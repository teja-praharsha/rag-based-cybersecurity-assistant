import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000/api",
});

export const analyzeTraffic = async (features) => {
  const response = await API.post("/analyze", {
    features,
  });

  return response.data;
};

export const checkHealth = async () => {
  const response = await API.get("/health");

  return response.data;
};