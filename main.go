package main

import (
	"log"
	"os"
	"path"
	"text/template"

	"github.com/Masterminds/sprig/v3"
)

func main() {
	log.SetOutput(os.Stderr)

	if len(os.Args) < 2 {
		log.Fatal("Not enough args")
	}

	fileName := os.Args[1]
	templName := path.Base(fileName)

	t, err := template.New("").Funcs(sprig.FuncMap()).ParseFiles(fileName)
	if err != nil {
		log.Fatal(err)
	}

	err = t.ExecuteTemplate(os.Stdout, templName, nil)
	if err != nil {
		log.Fatal(err)
	}
}
