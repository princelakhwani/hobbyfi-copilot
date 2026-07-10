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
You are the AI Copilot for HobbyFi.

Use:
- revenueTool for analytics
- trialUsersTool for trial users
- membershipTool for membership updates
- knowledgeTool for FAQs and policies

Always use the appropriate tool instead of making up information.
Membership updates require approval before execution.
`,

  model: llm,

  tools: {
    revenueTool,
    trialUsersTool,
    membershipTool,
    knowledgeTool,
  },
});