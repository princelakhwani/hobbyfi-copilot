type SessionMemory = {
  lastUserEmail?: string;
  lastUserName?: string;
  lastIntent?: string;
};

const sessions = new Map<string, SessionMemory>();

export function getMemory(sessionId: string) {
  if (!sessions.has(sessionId)) {
    sessions.set(sessionId, {});
  }

  return sessions.get(sessionId)!;
}

export function updateMemory(
  sessionId: string,
  data: Partial<SessionMemory>
) {
  const memory = getMemory(sessionId);

  Object.assign(memory, data);
}