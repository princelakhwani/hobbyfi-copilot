import { Agent } from "@mastra/core/agent";

import { revenueTool } from "../tools/revenue-tool";
import { llm } from "../config/models";

export const analyticsAgent = new Agent({
  id: "analytics-agent",

  name: "Analytics Agent",

  instructions: `
You answer vendor analytics questions.

Always use the revenue tool.

Never estimate revenue yourself.
`,

  model: llm,

  tools: {
    revenueTool,
  },
});