export enum WorkflowState {
  PENDING = "PENDING",
  APPROVED = "APPROVED",
  REJECTED = "REJECTED",
}

export interface ApprovalRequest {
  email: string;
  days: number;
  state: WorkflowState;
}

export function createApproval(
  email: string,
  days: number
): ApprovalRequest {
  return {
    email,
    days,
    state: WorkflowState.PENDING,
  };
}