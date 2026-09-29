"""
A Letter for You Nini
First Page
"""

LETTER_FIRST_PAGE = """
A Letter for you nini

and this is the letter I honestly don't know how to start this without sounding cheesy, but I guess I'll just say what I feel.

You mean a lot to me. Probably more than I know how to explain.

Somehow, you became one of those people I think about without even meaning to. I'll be doing something completely random and suddenly I'll remember something you said, your smile, or some little moment we had together. And honestly, those little things mean more to me than you probably realize.

I don't think you know how much your presence affects me. You can make a bad day feel better just by talking to me. Sometimes even seeing your name pop up on my phone is enough to make me smile like an idiot.

And I know I don't always say it, but I really appreciate you.

I appreciate the way you listen.
The way you make me laugh.
The way you can make ordinary moments feel special without even trying.

I also want you to know that you don't have to be perfect around me. You don't have to pretend that everything is okay all the time. You can have bad days, you can be quiet, you can be unsure of yourself. I won't think any less of you.

I like you for who you are, not for some perfect version of you.

Sometimes I get scared of how much I care because I know that when someone becomes important to you, they can also become someone you can miss, worry about, and care about way too much.

But even with that fear, I'm still grateful.

I'm grateful that I met you.
Grateful for every conversation.
Grateful for every laugh.
Grateful for every little memory that somehow became important to me.

I don't know what the future looks like, and I don't want to make promises about things I can't control.

I just know that right now, you're someone I genuinely care about. Someone I want to keep in my life. Someone I want to make more memories with.

And if you ever forget how special you are, I hope you remember that there is someone out here who thinks you're pretty amazing exactly as you are.

I may not always know the right thing to say.

I may not always show it.

But I hope you know that I care about you more than I probably say.

And honestly...

I'm really glad it's you.
"""

class LetterCode:
    """
    A special letter code that stores and manages your heartfelt message
    """
    
    def __init__(self):
        self.first_page = LETTER_FIRST_PAGE
        self.pages = [self.first_page]
    
    def get_first_page(self):
        """Retrieve the first page of the letter"""
        return self.first_page
    
    def get_all_pages(self):
        """Retrieve all pages of the letter"""
        return self.pages
    
    def add_page(self, content):
        """Add a new page to the letter"""
        self.pages.append(content)
        return f"Page {len(self.pages)} added successfully"
    
    def display_letter(self):
        """Display the complete letter"""
        print("="*60)
        print("A LETTER FOR YOU")
        print("="*60)
        for i, page in enumerate(self.pages, 1):
            print(f"\n--- PAGE {i} ---\n")
            print(page)
            print("\n")
        print("="*60)
    
    def letter_summary(self):
        """Get a summary of the letter"""
        return {
            "total_pages": len(self.pages),
            "character_count": sum(len(page) for page in self.pages),
            "word_count": sum(len(page.split()) for page in self.pages)
        }


# Example usage
if __name__ == "__main__":
    # Create your letter code
    letter = LetterCode()
    
    # Display the letter
    letter.display_letter()
    
    # Get letter statistics
    stats = letter.letter_summary()
    print(f"\nLetter Statistics:")
    print(f"Total Pages: {stats['total_pages']}")
    print(f"Total Words: {stats['word_count']}")
    print(f"Total Characters: {stats['character_count']}")
