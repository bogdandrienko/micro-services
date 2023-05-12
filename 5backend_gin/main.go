package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"io/ioutil"
	"math/rand"
	"net/http"
	"os"
	"time"
)

type Log struct {
	Id    int    `json:"id"`
	Title string `json:"title"`
	Value int    `json:"value"`
}

func write() {
	file, err := os.OpenFile("log.txt", os.O_RDWR|os.O_CREATE|os.O_APPEND, 0644)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer file.Close()

	_, err = file.WriteString(time.Now().Format("02-01-2006  15:04:05\n"))
	if err != nil {
		fmt.Println(err)
		return
	}
	return
}

func temporary() {
	resp, err := http.Get("https://www.google.com")
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()

	// Чтение ответа
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		panic(err)
	}

	// Вывод ответа на экран
	fmt.Println(string(body))
}

func main() {
	r := gin.Default()
	r.GET("/api", func(c *gin.Context) {
		// todo LOGIC
		go write()
		// todo LOGIC

		temporary()

		// todo LOGIC
		var logs []Log
		for i := 1; i <= 100; i += 1 {
			logs = append(logs, Log{
				Id: i, Title: fmt.Sprintf("Title i'm Gin %d", i), Value: rand.Intn(1000),
			})
		}
		c.JSON(http.StatusOK, logs)
	})
	if err := r.Run("0.0.0.0:8005"); err != nil {
		panic(err)
	}
}
