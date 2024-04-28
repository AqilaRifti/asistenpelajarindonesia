import requests
import pickle
from chromadb import Documents, EmbeddingFunction, Embeddings
from langchain.vectorstores.chroma import Chroma

# Replace the empty string with your model id below
model_id = "6wgzkv6q"
baseten_api_key = "Z1YSJldf.1KGF2f0sWIJ9u4wRsmSI7RvnXDix5CW3"

chunks_file = open('/Users/aqila/BIA/APIGPT/cache/SMP-ALL-185D-5000CS-500CO-V1.cache', 'rb')
chunks = chunks_file.read()
chunks_pickled = pickle.loads(chunks)
chunks_file.close()
print(chunks_pickled[1:3])
print(len(chunks_pickled))
exit()
class MyEmbeddingFunction(EmbeddingFunction):
    def __call__(self, inputs: Documents) -> Embeddings:
        embeddings = []
        # Call model endpoint
        def get_page_contents(inputs):
            page_contents = []
            for i in range(len(inputs)):
                page_contents.append(inputs[i].page_content)
            return page_contents
        data = {
            "texts": get_page_contents(inputs),
            "task_type": "search_query",
            "dimensionality": 768
        }
        res = requests.post(
            f"https://model-{model_id}.api.baseten.co/production/predict",
            headers={"Authorization": f"Api-Key {baseten_api_key}"},
            json=data
        )
        embeddings = res.json()
        return embeddings
    
    def embed_text(self, text):
        data = {
            "texts": [text],
            "task_type": "search_query",
            "dimensionality": 768
        }
        res = requests.post(
            f"https://model-{model_id}.api.baseten.co/production/predict",
            headers={"Authorization": f"Api-Key {baseten_api_key}"},
            json=data
        )
        return res.json()

    def embed_documents(self, texts):
        """Embed a list of documents using GPT4All.

        Args:
            texts: The list of texts to embed.

        Returns:
            List of embeddings, one for each text.
        """

        embeddings = [self.embed_text(text) for text in texts[0]]

        return [list(map(float, e)) for e in embeddings]
    
    def embed_query(self, text: str):
        return self.embed_documents([text])
    
db = Chroma.from_documents(
    # chunks_pickled, 
    chunks_pickled[0:3],
    embedding=MyEmbeddingFunction(),
    persist_directory="./order-45"
)
db.persist()
db = Chroma(persist_directory="./order-46", embedding_function=MyEmbeddingFunction)

# Search the DB.
results = db.similarity_search_with_relevance_scores("a", k=7)
print(results)