import { Agent } from "@mastra/core/agent";

import { revenueTool } from "../tools/revenue-tool";
import { trialUsersTool } from "../tools/trial-users-tool";
import { membershipTool } from "../tools/membership-tool";

export const supervisorAgent = new Agent({
  id: "supervisor-agent",

  name: "HobbyFi Copilot",

  instructions: `
You are the AI Copilot for HobbyFi vendors.

Use the appropriate tool whenever possible.

Analytics:
- Revenue

CRM:
- Trial Users
- Membership Updates

Never invent data.

Membership updates require vendor approval before execution.
`,

  model: "openai/gpt-4.1-mini",

  tools: {
    revenueTool,
    trialUsersTool,
    membershipTool,
  },
});