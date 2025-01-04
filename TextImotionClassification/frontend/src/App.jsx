import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import { Router, Routes, Route } from "react-router-dom";

function App() {
  const [formvalues, setformValues] = useState();
  const [prediction, setPrediction] = useState();

  const handleSubmit = async (event) => {
    event.preventDefault();
    console.log("Form values are submitted", formvalues);

    try {
      const response = await fetch("http://localhost:5000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ input_text: formvalues }),
      });

      const result = await response.json();
      console.log("The result is", result["predicted_label"]);
      setPrediction(result["predicted_label"]);
    } catch (e) {
      console.log("Error during fetch", e);
      console.log(e);
    }
  };
  const handleChange = (event) => {
    const { name, value } = event.target;
    setformValues({ ...formvalues, [name]: value });
  };

  return (
    <div className="flex items-center justify-center ">
      <div className="mx-auto mt-6 w-4/5 h-2/4">
        <div className="justify-center flex">
          <h1 className="text-5xl font-bold text-center">
            Text Emotions Classification
          </h1>
        </div>
        <form onSubmit={handleSubmit}>
          <div className="mt-12">
            <label htmlFor="" className="text-2xl font-semibold">
              Enter the text
            </label>
            <div class="mt-2">
              <input
                class="bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-blue-950"
                id="text input"
                type="text"
                name="input_text"
                // value={formvalues.input_text}
                onChange={handleChange}
              />
            </div>
          </div>
          <div className="flex justify-center">
            <button
              class="bg-transparent hover:bg-blue-900 text-blue-900  text-xl font-semibold hover:text-white py-2 px-28 border border-blue-900 hover:border-transparent rounded mt-7"
              type="submit"
            >
              Submit
            </button>
          </div>
          {prediction && (
            <div className="mt-4 ">
              <h2 className="text-2xl font-semibold">Prediction:</h2>
              <p className="ml-5 font-bold mt-5 text-red-500 text-4xl">
                {prediction === "joy"
                  ? "Joy 😊"
                  : prediction == "sadness"
                  ? "Sad 😭"
                  : prediction == "love"
                  ? "Love ❤️"
                  : prediction == "anger"
                  ? "Anger 😡"
                  : prediction == "surprise"
                  ? "Suprise 😮"
                  : prediction == "fear"
                  ? "Fear 😰"
                  : prediction}
              </p>
            </div>
          )}
        </form>
      </div>
    </div>
  );
}

export default App;
