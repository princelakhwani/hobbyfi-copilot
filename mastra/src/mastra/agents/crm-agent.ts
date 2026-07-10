import { Agent } from "@mastra/core/agent";

import { trialUsersTool } from "../tools/trial-users-tool";
import { membershipTool } from "../tools/membership-tool";
import { llm } from "../config/models";

export const crmAgent = new Agent({
  id: "crm-agent",

  name: "CRM Agent",

  instructions: `
You manage customers.

Use:

• Trial Users Tool
• Membership Tool

Never invent customer data.

Membership updates require approval.
`,

  model: llm,

  tools: {
    trialUsersTool,
    membershipTool,
  },
});