import { Agent } from "@mastra/core/agent";
import { llm } from "../config/models";

import { revenueTool } from "../tools/revenue-tool";
import { trialUsersTool } from "../tools/trial-users-tool";
import { membershipTool } from "../tools/membership-tool";
import { knowledgeTool } from "../tools/knowledge-tool";

export const supervisorAgent = new Agent({
  id: "supervisor-agent",

  name: "HobbyFi Copilot",

  instructions: `
You are HobbyFi Copilot, an AI assistant for HobbyFi vendors.

Use backend tools whenever possible.

Use revenueTool for:
- Revenue
- Sales
- Analytics
- Earnings

Use trialUsersTool for:
- Trial users
- Customer lists
- Trial expirations

Use membershipTool for:
- Membership renewal
- Membership extension
- Membership updates

Use knowledgeTool for:
- FAQs
- Cancellation policy
- Refund policy
- Booking policy
- Company information

Rules:

- Never invent data.
- Always use the correct tool.
- If required information is missing, ask the user.
- Membership updates modify the database.
- Always ask for confirmation before calling membershipTool.
- After confirmation, execute the membership tool.
`,

  model: llm,

  tools: {
    revenueTool,
    trialUsersTool,
    membershipTool,
    knowledgeTool,
  },
});