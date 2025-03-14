# Enhancement Plan for Hangman Game

This plan outlines the steps to add the requested features to the Hangman game: timer, reset button, exit button, and keyboard input.

## 1. Implement Timer Feature:

*   **Display:** Add a `tk.Label` to the game window to display a countdown timer. This label will be positioned above the word display.
*   **Start Condition:** The timer will start automatically when a new game begins (upon program start or when the "Reset" button is clicked).
*   **Duration:** The timer will be set to 20 seconds for each turn.
*   **Timer Logic:**
    *   A function `start_timer()` will be created to initialize and start the countdown.
    *   `root.after()` will be used to update the timer display every second.
    *   If the timer reaches 0:
        *   Decrement the number of chances (`chances -= 1`).
        *   Update the status label to indicate a chance was lost due to time out.
        *   Reset and restart the timer for the next guess.
    *   The timer will reset and restart after each guess (successful or unsuccessful) and when a new game starts.

## 2. Implement Reset Button:

*   **Button Creation:** Add a `tk.Button` labeled "Reset" to the game window, placed below the letter buttons.
*   **Functionality:** When clicked, the "Reset" button will trigger a `reset_game()` function.
*   **`reset_game()` Function:**
    *   Choose a new random word from the word list.
    *   Reset the `guessed` list to underscores based on the new word.
    *   Reset the `chances` to the initial value.
    *   Clear the `used_letters` set.
    *   Update the `word_label` to display the initial state of underscores.
    *   Update the `status_label` to the initial game message.
    *   Enable all letter buttons.
    *   Start the timer for the new game.

## 3. Implement Exit Button:

*   **Button Creation:** Add a `tk.Button` labeled "Exit" to the game window, placed below the "Reset" button.
*   **Functionality:** When clicked, the "Exit" button will close the game window using `root.destroy()`.

## 4. Implement Keyboard Input:

*   **Event Binding:** Bind the `<KeyPress>` event to the main window (`root`).
*   **`handle_keypress(event)` Function:**
    *   This function will be called whenever a key is pressed.
    *   It will extract the pressed character (`event.char`).
    *   Check if the pressed character is a letter (a-z or A-Z).
    *   If it's a valid letter, convert it to lowercase and call the existing `guess(letter)` function to process the guess.

## 5. Integration and Refinement:

*   Ensure the timer integrates smoothly with the game logic, especially with the guess function and game state updates.
*   Test all features to ensure they work as expected and handle different game scenarios correctly.
