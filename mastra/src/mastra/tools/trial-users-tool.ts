import { createTool } from "@mastra/core/tools";
import { z } from "zod";
import backend from "../services/backend-client";

export const trialUsersTool = createTool({
  id: "trial-users-tool",

  description:
    "Retrieve all users currently on trial for a given sport.",

  inputSchema: z.object({
    sport: z.string(),
  }),

  outputSchema: z.object({
    count: z.number(),
    users: z.array(
      z.object({
        name: z.string(),
        email: z.string(),
        trial_remaining: z.number(),
      })
    ),
  }),

  execute: async ({ sport }) => {
    const { data } = await backend.get("/users/trial", {
      params: {
        sport,
      },
    });

    return data;
  },
});