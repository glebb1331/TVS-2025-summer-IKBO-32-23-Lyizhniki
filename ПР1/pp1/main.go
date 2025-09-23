package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"net/http"
	"os"
	"time"
)

const apiKey = "7b10c38e4746f83edb805a1dbf105ce2" // 1 неверный api ключ, верный - 7b10c38e4746f83edb805a1dbf105ce1

type Country struct {
	Capital  string
	Timezone string
}

var countries = map[string]Country{
	"Россия":    {"Moscow", "Asia/Dubai"}, //2
	"Китай":     {"Beijing,CN", "Asia/Shanghai"},
	"Япония":    {"Tokyo", "Asia/Tokyo"},
	"Испания":   {"Barcelona", "Europe/Madrid"},     //3
	"Австралия": {"McMurdo,AQ", "Australia/Sydney"}, //4
}

type WeatherResponse struct {
	Main struct {
		Temp float64 `json:"temp"`
	} `json:"main"`
}

func getWeather(city string) (float64, error) {
	url := fmt.Sprintf("https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s&units=metric", city, apiKey)
	resp, err := http.Get(url)
	if err != nil {
		return 0, err
	}
	defer resp.Body.Close()

	var weather WeatherResponse
	if err := json.NewDecoder(resp.Body).Decode(&weather); err != nil {
		return 0, err
	}
	return weather.Main.Temp, nil
}

func main() {
	fmt.Println("Выберите страну:")
	for name := range countries {
		fmt.Println("-", name)
	}

	var choice string
	fmt.Print("Введите страну: ")
	fmt.Scanln(&choice)

	country, ok := countries[choice]
	if !ok {
		fmt.Println("Ошибка: страна не найдена!")
		waitForExit()
		return
	}

	loc, err := time.LoadLocation(country.Timezone)
	if err != nil {
		fmt.Println("Ошибка временной зоны!")
		waitForExit()
		return
	}
	currentTime := time.Now().In(loc).Format("15:04:05")

	temp, err := getWeather(country.Capital)
	if err != nil {
		fmt.Println("Ошибка получения погоды!")
		waitForExit()
		return
	}

	fmt.Printf("\nСтолица: %s\nВремя: %s\nТемпература: %.1f°F\n", //5 ошибка: показываем Фаренгейт, но получаем Цельсий
		country.Capital, currentTime, temp)

	waitForExit()
}

func waitForExit() {
	fmt.Println("\nНажмите Enter, чтобы выйти...")
	bufio.NewReader(os.Stdin).ReadBytes('\n')
}
