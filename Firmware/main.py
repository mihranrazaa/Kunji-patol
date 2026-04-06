import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.modtap import ModTap

keyboard = KMKKeyboard()

keyboard.modules.append(Layers())
keyboard.modules.append(ModTap())
keyboard.extensions.append(MediaKeys())


keyboard.row_pins = (
    board.GP0,   # Row 0
    board.GP1,   # Row 1  
    board.GP2,   # Row 2
    board.GP3,   # Row 3
    board.GP4,   # Row 4
    board.GP5,   # Row 5
)

keyboard.col_pins = (
    board.GP6,   # Col 0
    board.GP7,   # Col 1
    board.GP8,   # Col 2
    board.GP9,   # Col 3
    board.GP10,  # Col 4
    board.GP11,  # Col 5
    board.GP12,  # Col 6
    board.GP13,  # Col 7
    board.GP14,  # Col 8
    board.GP15,  # Col 9
    board.GP16,  # Col 10
    board.GP17,  # Col 11
    board.GP18,  # Col 12
    board.GP19,  # Col 13
    board.GP20,  # Col 14
    board.GP21,  # Col 15
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW



# layers
keyboard.keymap = [
    # Layer 0
    [
        KC.ESC,    KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,  KC.PSCR, KC.SLCK, KC.PAUS,
        KC.GRV,    KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQL,  KC.BSPC,          KC.INS,  KC.HOME, KC.PGUP,
        KC.TAB,    KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.BSLS,          KC.DEL,  KC.END,  KC.PGDN,
        KC.CAPS,   KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT,          KC.ENT,
        KC.LSFT,   KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH,          KC.RSFT,                            KC.UP,
        KC.LCTL,   KC.LGUI, KC.LALT,                   KC.SPC,                            KC.RALT, KC.RGUI, KC.MENU, KC.RCTL,          KC.LEFT, KC.DOWN, KC.RGHT,
    ],
    
    # Layer 1
    [
        KC.TRNS,   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS,   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,          KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS,   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,          KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS,   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,          KC.TRNS,
        KC.TRNS,   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,          KC.TRNS,                            KC.VOLU,
        KC.TRNS,   KC.TRNS, KC.TRNS,                   KC.TRNS,                            KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,          KC.MPRV, KC.VOLD, KC.MNXT,
    ],
]

keyboard.debounce_time = 10

keyboard.tap_time = 200

if __name__ == '__main__':
    keyboard.go()