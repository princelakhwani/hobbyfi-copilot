import { Agent } from "@mastra/core/agent";

import { membershipTool } from "../tools/membership-tool";
import { trialUsersTool } from "../tools/trial-users-tool";

export const crmAgent = new Agent({
  id: "crm-agent",

  name: "CRM Agent",

  instructions: `
You manage users.

Always use tools.

You answer:

- Trial Users
- Membership
- User Information

Any update requires approval.
`,

  model: "openai/gpt-4.1-mini",

  tools: {
    membershipTool,
    trialUsersTool,
  },
});