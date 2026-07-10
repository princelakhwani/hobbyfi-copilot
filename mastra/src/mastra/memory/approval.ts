type PendingApproval = {
  email: string;
  days: number;
};

export let pendingApproval: PendingApproval | null = null;

export function setPendingApproval(data: PendingApproval) {
  pendingApproval = data;
}

export function clearPendingApproval() {
  pendingApproval = null;
}