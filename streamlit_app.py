import streamlit as st

def palindrome(word: str) -> bool:
    return word == word[::-1]

def main():
    "for i in range(1000):"  # This will ask the user 1000 times; consider using a while loop for indefinite tries
    st.title("Palindrome Checker")
    word = st.text_input("Can your small brain think of a palindrome? Throw a word:")
    if word:
        if palindrome(word):
            st.success("Congrats, you've finally achieved something in life.")
        else:
            st.error("Wow, you've got an IQ of a potato.")

if __name__ == "__main__":
    main()