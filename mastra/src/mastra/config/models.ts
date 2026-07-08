import "dotenv/config";

import { openai } from "@ai-sdk/openai";

export const llm = openai(
    process.env.MODEL_NAME || "gpt-4.1-mini"
);

export const FASTAPI_BASE_URL =
    process.env.FASTAPI_BASE_URL ||
    "http://localhost:8000";