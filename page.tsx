"use client"
import { useState } from 'react'
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"
import { Textarea } from "@/components/ui/textarea"

export default function Home() {
  const [inputText, setInputText] = useState("");
  const [response, setResponse] = useState("");
  return (
    <main className="flex min-h-screen flex-col p-24">
      <h1 className="mb-4 text-center text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl dark:text-white">EMLO S17 - Text Generation</h1>
      <div className="flex w-full max-w-sm items-center space-x-2 space-y-8">
        <Input type="text" className="text-black" placeholder="Enter prompt" onChange={(e) => {
          setInputText(e.target.value)
        }} />
        <Button className="space-y-8" onClick={() => {
          console.log(inputText)

          fetch(`https://secure-evident-hyena.ngrok-free.app/textgen?inp_text=${inputText}`, {
            method: 'POST',
            // body: formdata,
            redirect: 'follow'
          })
            .then((response) => response.text())
            .then((result) => {
              setResponse(result);
            })
            .catch((error) => console.log("error", error));
        }}>submit</Button>
      </div>
      {/* {response} */}
      <div className='space-x-2 space-y-2'>
        <Textarea placeholder={response} />
      </div>
    </main>
  )
}