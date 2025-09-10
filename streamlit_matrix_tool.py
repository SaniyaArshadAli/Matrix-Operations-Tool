import streamlit as st
import numpy as np

def parse_matrix_input(text_input):
    """Parses a string of text into a NumPy array."""
    try:
        rows = text_input.strip().split('\n')
        matrix_data = []
        for row in rows:
            elements = [float(x) for x in row.split()]
            matrix_data.append(elements)
        return np.array(matrix_data)
    except (ValueError, IndexError):
        return None

def main():
    """Main function to run the Streamlit app."""
    st.set_page_config(layout="wide")
    st.title("Matrix Operations Tool")

    tab1, tab2 = st.tabs(["Matrix Operations", "Cheat Sheet"])

    with tab1:
        st.header("Perform Operations on Matrices")
        
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Matrix A")
            matrix_a_text = st.text_area("Enter elements for Matrix A (space-separated per row):", height=200)

        with col2:
            st.subheader("Matrix B")
            matrix_b_text = st.text_area("Enter elements for Matrix B (space-separated per row):", height=200)
            
        st.markdown("---")
        
        st.subheader("Select an Operation")
        op_col1, op_col2, op_col3, op_col4, op_col5 = st.columns(5)
        
        result = None
        error_message = ""
        
        try:
            A = parse_matrix_input(matrix_a_text)
            B = parse_matrix_input(matrix_b_text)
            
            if A is not None and op_col1.button("Addition (+)", use_container_width=True):
                if B is not None and A.shape == B.shape:
                    result = A + B
                else:
                    error_message = "Matrices must have the same dimensions for addition."
            
            if A is not None and op_col2.button("Subtraction (-)", use_container_width=True):
                if B is not None and A.shape == B.shape:
                    result = A - B
                else:
                    error_message = "Matrices must have the same dimensions for subtraction."
            
            if A is not None and op_col3.button("Multiplication (×)", use_container_width=True):
                if B is not None and A.shape[1] == B.shape[0]:
                    result = np.dot(A, B)
                else:
                    error_message = "The number of columns in Matrix A must equal the number of rows in Matrix B."
            
            if A is not None and op_col4.button("Transpose (T)", use_container_width=True):
                result = A.T
            
            if A is not None and op_col5.button("Determinant", use_container_width=True):
                if A.shape[0] == A.shape[1]:
                    result = np.linalg.det(A)
                else:
                    error_message = "The determinant can only be calculated for a square matrix."
        
        except Exception as e:
            error_message = f"An error occurred: {e}"

        st.markdown("---")
        st.subheader("Result")
        
        if result is not None:
            if isinstance(result, np.ndarray):
                st.dataframe(result, use_container_width=True)
            else:
                st.write(result)
        elif error_message:
            st.error(error_message)
        else:
            st.info("Enter matrices and select an operation to see the result.")

    with tab2:
        st.header("Matrix Operations Cheat Sheet")
        st.markdown("""
        Understanding the rules for each operation is essential to avoid errors.

        ---

        ### Matrix Addition and Subtraction
        * **Rule:** Both matrices must have the exact same dimensions.
        * **Example:** You can add a $2 \times 3$ matrix to another $2 \times 3$ matrix, but not to a $3 \times 2$ matrix.
        * **Result:** The resulting matrix will have the same dimensions as the original matrices.

        ---

        ### Matrix Multiplication
        * **Rule:** For two matrices, $A$ and $B$, the number of **columns** in matrix $A$ must be equal to the number of **rows** in matrix $B$.
        * **Example:** A $2 \times 3$ matrix can be multiplied by a $3 \times 4$ matrix.
        * **Result:** The resulting matrix will have the dimensions of the rows of $A$ and the columns of $B$. In the example above, the result would be a $2 \times 4$ matrix.

        ---

        ### Matrix Transpose
        * **Rule:** No specific rules for this operation. You can transpose any matrix regardless of its dimensions.
        * **Description:** The rows become the columns and the columns become the rows.
        * **Example:** The transpose of a $2 \times 3$ matrix is a $3 \times 2$ matrix.

        ---

        ### Matrix Determinant
        * **Rule:** This operation can only be performed on a **square matrix**.
        * **Description:** A single scalar value calculated from the elements of a square matrix.
        * **Example:** The determinant can be found for a $2 \times 2$ or a $3 \times 3$ matrix, but not for a $2 \times 3$ matrix.
        """)

if __name__ == '__main__':
    main()
