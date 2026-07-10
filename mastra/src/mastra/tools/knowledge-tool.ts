import axios from "axios";
import { z } from "zod";
import { createTool } from "@mastra/core/tools";

export const knowledgeTool = createTool({
  id: "knowledge-tool",

  description: "Answer questions using the HobbyFi knowledge base.",

  inputSchema: z.object({
    question: z.string(),
  }),

  outputSchema: z.object({
    answer: z.string(),
  }),

  execute: async ({ question }) => {
    const response = await axios.post(
      "http://127.0.0.1:8000/knowledge/ask",
      {
        question,
      }
    );

    return response.data;
  },
});