from fastapi import APIRouter
import numpy as np

router = APIRouter()

def generate_random_matrix(size: int) -> list:
    return np.random.randint(1, 10, size=(size, size)).tolist()

def multiply_matrices(matrix_a: list, matrix_b: list) -> list:
    return np.dot(matrix_a, matrix_b).tolist()

@router.get("/multiply_matrices")
def multiply_matrices_endpoint() -> dict:
    size = 10
    matrix_a = generate_random_matrix(size)
    matrix_b = generate_random_matrix(size)
    product = multiply_matrices(matrix_a, matrix_b)
    return {
        "matrix_a": matrix_a,
        "matrix_b": matrix_b,
        "product": product
    }

@router.get('/')
def hello_world() -> dict:
    return {'msg': 'Hello, World!'}
