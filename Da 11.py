from neo4j import GraphDatabase 
import tweepy 
import tensorflow as tf 
from tensorflow.keras.preprocessing.text import Tokenizer 
from tensorflow.keras.preprocessing.sequence import pad_sequences 

# Neo4j connection details 
NEO4J_URI = "bolt://localhost:7687" 
NEO4J_USER = "neo4j" 
NEO4J_PASSWORD = "password" 

# Connect to Neo4j 
class Neo4jConnector: 
    def __init__(self, uri, user, password): 
        self.driver = GraphDatabase.driver(uri, auth=(user, password)) 

    def close(self): 
        self.driver.close() 

    def insert_data(self, tweet_id, user_name, text, sentiment, keywords): 
        with self.driver.session() as session: 
            session.write_transaction( 
                self._create_tweet, tweet_id, user_name, text, sentiment, keywords 
            ) 

    @staticmethod 
    def _create_tweet(tx, tweet_id, user_name, text, sentiment, keywords): 
        query = """ 
        MERGE (u:User {name: $user_name}) 
        MERGE (t:Tweet {id: $tweet_id, text: $text, sentiment: $sentiment}) 
        MERGE (u)-[:POSTED]->(t) 
        WITH t 
        UNWIND $keywords AS keyword 
        MERGE (k:Keyword {name: keyword}) 
        MERGE (t)-[:MENTIONS]->(k) 
        """ 
        tx.run( 
            query, 
            tweet_id=tweet_id, 
            user_name=user_name, 
            text=text, 
            sentiment=sentiment, 
            keywords=keywords, 
        ) 

# Initialize Neo4j 
neo4j_conn = Neo4jConnector(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD) 

# Pre-trained model path 
MODEL_PATH = "sentiment_model.h5" 
model = tf.keras.models.load_model(MODEL_PATH) 

# Tokenizer configuration 
MAX_SEQUENCE_LENGTH = 100 
tokenizer = Tokenizer(num_words=10000) 

def preprocess_tweet(tweet): 
    sequences = tokenizer.texts_to_sequences([tweet]) 
    padded = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH) 
    return padded 

def predict_sentiment(tweet): 
    processed_tweet = preprocess_tweet(tweet) 
    prediction = model.predict(processed_tweet)[0][0] 
    return "Positive" if prediction > 0.5 else "Negative" if prediction < 0.5 else "Neutral" 

# Twitter Stream Listener 
class MyStreamListener(tweepy.StreamListener): 
    def on_status(self, status): 
        try: 
            tweet_id = status.id_str 
            user_name = status.user.screen_name 
            text = status.text 
            sentiment = predict_sentiment(text) 
            keywords = ["your_brand_name"]  # Extract keywords dynamically if needed 
            neo4j_conn.insert_data(tweet_id, user_name, text, sentiment, keywords) 
            print(f"Tweet: {text}\nSentiment: {sentiment}\n") 
        except Exception as e: 
            print(f"Error: {str(e)}") 

    def on_error(self, status_code): 
        print(f"Error: {status_code}") 
        return False 

# Twitter API setup 
API_KEY = "your_api_key" 
API_SECRET_KEY = "your_api_secret_key" 
ACCESS_TOKEN = "your_access_token" 
ACCESS_TOKEN_SECRET = "your_access_token_secret" 

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY) 
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET) 

stream_listener = MyStreamListener() 
stream = tweepy.Stream(auth=auth, listener=stream_listener) 

# Track specific keywords 
BRAND_KEYWORDS = ["your_brand_name"] 
stream.filter(track=BRAND_KEYWORDS, is_async=True)
