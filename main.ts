let delta_x = 0
let delta_y = 0
let delta_loger = 0
let dx = 0
let dy = 0
let x = 0
let y = 0
control.onEvent(EventBusSource.MICROBIT_ID_BUTTON_A, EventBusValue.MICROBIT_BUTTON_EVT_CLICK, function () {
    music.playMelody("C5 B A G F E D C ", 500)
})
function lines (x0: number, y0: number, x1: number, y1: number) {
    delta_x = x1 - x0
    delta_y = y1 - y0
    delta_loger = Math.max(Math.abs(delta_x), Math.abs(delta_y))
    dx = delta_x / delta_loger
    dy = delta_y / delta_loger
    x = x0 + 0.5
    y = y0 + 0.5
    for (let index = 0; index < delta_loger + 1; index++) {
        disp_star(x, y)
        x += dx
        y += dy
    }
}
function disp_star (x: number, y: number) {
    led.plot(x, y)
    basic.pause(100)
    led.unplot(x, y)
}
basic.forever(function () {
    control.raiseEvent(
    EventBusSource.MICROBIT_ID_BUTTON_A,
    EventBusValue.MICROBIT_BUTTON_EVT_CLICK
    )
    basic.clearScreen()
    lines(randint(0, 4), 0, randint(0, 4), 4)
    basic.pause(randint(100, 10000))
})
