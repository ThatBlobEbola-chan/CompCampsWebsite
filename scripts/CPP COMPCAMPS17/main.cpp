// comment woo

#include <iostream>
#include <string.h>
#include <stdlib.h> // srand,rand
#include <time.h> // to use the system clock
using namespace std;
int lives = 3;
int number;
int guess;

bool guessing (int number);

void levelOne();
void levelTwo();

int main () //int = integer = whole positive/negative numbers
{
    //random number: 1-5. 5-25, 25-50, 50-100
    cout << "Come on and slam, and welcome to the jam." << endl;
    cout << "Guess the number correctly to make sweet dunks." << endl;

    srand (time(NULL));

    levelOne();

  return 0;
}

bool guessing (int number)
{
  cout << "Guess between 1-5." << endl;
  cin >> guess;
  lives--;
  do {

    //too high
    if (guess > number)
    {
      cout << "Too high, you moronic starfish" << endl;
      cin >> guess;
      lives--;
    }
    //too low
    if (guess < number)
    {
      cout << "Too low, you complete waste of molecules" << endl;
      cin >> guess;
      lives--;
    }

    if (guess == number)
    {
      cout << "Good job, but you're still a complete waste of moronic starfish molecules." << endl;
      lives++;
      return true;
    }
  } while (lives < 0);

  cout << "Game over you complete nutlord" << endl;
  return false;

}

void levelOne()
{
  number = rand() % 5 + 1;
  cout << number;
  if (guessing(number)) {
    levelTwo();
  }
}

void levelTwo()
{
  number = rand() % 25 + 5;
  cout << number;
  if (guessing(number)) {
    cout << "You won the game wow dang that was stanky" << endl;
  }
}
