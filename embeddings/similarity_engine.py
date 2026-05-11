from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_similarity(job_description, resume_text):

    # Convert texts into embeddings
    jd_embedding = model.encode([job_description])

    resume_embedding = model.encode([resume_text])

    # Calculate cosine similarity
    similarity_score = cosine_similarity(
        jd_embedding,
        resume_embedding
    )[0][0]

    # Convert to percentage
    return round(float(similarity_score) * 100, 2)