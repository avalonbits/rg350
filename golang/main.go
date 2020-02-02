package main

import (
	"fmt"

	"github.com/veandco/go-sdl2/sdl"
)

func main() {
	if err := sdl.Init(sdl.INIT_EVERYTHING); err != nil {
		panic(err)
	}
	defer sdl.Quit()

	sdl.JoystickEventState(sdl.ENABLE)
	var joy *sdl.Joystick
	if sdl.NumJoysticks() > 0 {
		joy = sdl.JoystickOpen(0)
		defer joy.Close()
	}

	window, err := sdl.CreateWindow("test", sdl.WINDOWPOS_UNDEFINED, sdl.WINDOWPOS_UNDEFINED,
		320, 240, sdl.WINDOW_FULLSCREEN_DESKTOP)
	if err != nil {
		panic(err)
	}
	defer window.Destroy()

	surface, err := window.GetSurface()
	if err != nil {
		panic(err)
	}
	surface.FillRect(nil, 0)

	rect := sdl.Rect{0, 0, 200, 200}
	surface.FillRect(&rect, 0xffff0000)
	window.UpdateSurface()

	running := true
	for running {
		for event := sdl.PollEvent(); event != nil; event = sdl.PollEvent() {
			switch event.(type) {
			case *sdl.QuitEvent:
				fmt.Println("Quit")
				running = false
				break
			case *sdl.KeyboardEvent:
				fmt.Println(sdl.KEYDOWN, event.GetType(), "Quit key")
				running = false
				break
			case *sdl.JoyAxisEvent:
				fmt.Println("Joy axis")
				running = false
				break
			}

		}
	}
}
