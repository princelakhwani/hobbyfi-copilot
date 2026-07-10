export function requiresApproval(action: string) {
  const writeActions = [
    "membership",
    "trial",
    "update",
    "delete",
    "extend",
  ];

  return writeActions.some((keyword) =>
    action.toLowerCase().includes(keyword)
  );
}