import { createTool } from "@mastra/core/tools";
import { z } from "zod";

import backend from "../services/backend-client";

export const revenueTool = createTool({
  id: "get-revenue",

  description: "Returns today's revenue for the vendor.",

  inputSchema: z.object({}),

  outputSchema: z.object({
    revenue: z.number(),
  }),

  execute: async () => {
    const response = await backend.get("/analytics/revenue");

    return {
      revenue: response.data.revenue,
    };
  },
});