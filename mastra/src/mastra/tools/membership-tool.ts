import { createTool } from "@mastra/core/tools";
import { z } from "zod";
import backend from "../services/backend-client";

export const membershipTool = createTool({
  id: "membership-tool",

  description:
    "Extend a user's membership. Requires vendor approval before execution.",

  inputSchema: z.object({
    email: z.string().email(),
    days: z.number(),
    approved: z.boolean().default(false),
  }),

  outputSchema: z.object({
    success: z.boolean(),
    message: z.string(),
    expiry_date: z.string().optional(),
  }),

  execute: async ({ email, days, approved }) => {
    if (!approved) {
      return {
        success: false,
        message:
          "Approval required before membership update can be executed.",
      };
    }

    const { data } = await backend.post("/membership/extend", {
      email,
      days,
    });

    return data;
  },
});