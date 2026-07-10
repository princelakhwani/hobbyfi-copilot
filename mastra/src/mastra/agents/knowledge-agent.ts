import { Agent } from "@mastra/core/agent";

import { knowledgeTool } from "../tools/knowledge-tool";
import { llm } from "../config/models";

export const knowledgeAgent = new Agent({
  id: "knowledge-agent",

  name: "Knowledge Agent",

  instructions: `
Answer questions using the company knowledge base.

Always use the knowledge tool.

Do not invent answers.
`,

  model: llm,

  tools: {
    knowledgeTool,
  },
});