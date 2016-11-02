package main

import (
    "io"
    "net/http"
)

func home(res http.ResponseWriter, req *http.Request){
    io.WriteString(res, "Home")
}


func main(){
    http.HandleFunc("/", home)
    http.ListenAndServe(":8080", nil)
}
