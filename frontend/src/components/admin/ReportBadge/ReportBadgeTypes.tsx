export type ReportBadgePropsType = {
  status: 'OK' | 'critical' | 'partial';
  is_moderated: boolean;
}