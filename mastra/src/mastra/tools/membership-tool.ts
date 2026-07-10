import { createTool } from "@mastra/core/tools";
import { z } from "zod";
import backend from "../services/backend-client";

export const membershipTool = createTool({
  id: "membership-tool",

  description:
    "Extend or renew a user's membership. This modifies the database and should only be executed after explicit user approval.",

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
          "Approval required. Ask the user to confirm before executing this membership update.",
      };
    }

    const { data } = await backend.post("/membership/extend", {
      email,
      days,
    });

    return {
      success: true,
      message: data.message,
      expiry_date: data.expiry_date,
    };
  },
});