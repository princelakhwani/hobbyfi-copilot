import { createTool } from "@mastra/core/tools";
import { z } from "zod";
import backend from "../services/backend-client";

export const revenueTool = createTool({
  id: "revenue-tool",

  description:
    "Retrieve today's revenue and financial analytics from the HobbyFi backend.",

  inputSchema: z.object({}),

  outputSchema: z.object({
    revenue: z.number(),
  }),

  execute: async () => {
    const { data } = await backend.get("/analytics/revenue");

    return {
      revenue: data.revenue,
    };
  },
});