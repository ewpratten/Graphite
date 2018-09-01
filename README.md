# Graphite
The generic graphics driver for Dirobium based devices

## Installation
First, make sure you have the [Dirobium emulator](https://github.com/Ewpratten/Dirobium) installed, and have set up an emulation environment \(Instructions on that can be found in the [Dirobium documentation](https://github.com/Ewpratten/Dirobium/blob/master/README.md)\)

Next, `cd` into the `devices/` directory of the emulation environment and run this command:
```bash
git clone https://github.com/Ewpratten/Graphite.git ./a
```

Note: This driver **MUST** be in device slot `a` if you are using the [Deuterium bootloader](https://github.com/Ewpratten/Deuterium), or if you don't know the internals of the emulator. Only **very** experienced users should change the device slot.

## How does it work?
Graphite uses an ascii based display emulator (built in to the driver) to display a 30x30 virtual screen in your terminal. Instead of using pixels to display graphics, Graphite is designed specifically for text and uses ascii chars to display text. Everything that is displayed on the screen, is stored in a *buffer file*. The buffer file allows you to keep text on the screen across reboots and also, change programs, then come back right where you left off.

## How do I use it?
Graphite uses the Dirobium device API. This makes calling the python code from assembly very easy.

To initalize the screen:
```
# Initalize mode
mov 1 e2
# call device 1 (graphite)
call 1

# Write mode
mov 2 e2
call 1
```

To set where you are going to draw a letter:
```
# set the collumn
mov 0 e5

# set the row
mov 0 e4

# call graphics driver
call 1
```

To write to the screen:
```
# set char to the letter "a"
mov 1 e3
call 1
```

The char codes are just all the numbers that match up with the english alphabet (1-26), and space (0)

## Example
Write *hello* to the screen:
```
# Init
mov 1 e2
call 1

mov 2 e2
call 1

# Cursor
mov 0 e4

# text
mov 8 e3
mov 0 e5
call 1

mov 5 e3
mov 1 e5
call 1

mov 12 e3
mov 2 e5
call 1

mov 12 e3
mov 3 e5
call 1

mov 15 e3
mov 4 e5
call 1
```