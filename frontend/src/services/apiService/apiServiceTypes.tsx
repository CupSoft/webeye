export type UserRegistrResponseTypes = {
  email: string;
  uuid: string;
  is_admin: boolean;
}

export type UserRegistrRequestTypes = {
  email: string;
  password: string;
}

export type UserLoginResponseTypes = {
  access_token: string,
  token_type: string,
}

export type SourceGetTypes = {
  name: string;
  status: 'OK' | 'partial' | 'critical';
  uuid: string;
  rating: number;
  url: string;
}

export type SourceGetRequestTypes = {
  limit?: number;
  skip?: number;
}

export type UserStoreTypes = {
  isAuth: boolean;
  isAdmin: boolean;
  email: string;
  uuid: string;
}

export type SocialReporGetTypes = {
  status: 'OK' | 'partial' | 'critical';
  social_network: 'VK' | 'OK',
  link: string;
  uuid: string;
  created_at: string;
  snippet: string
  resource_uuid?: string;
}

export type ReviewGetTypes = {
  datetime: string;
  text: string;
  stars: number;
  uuid: string;
}

export type SubscriptionPostTypes = {
  to_telegram: boolean;
  to_email: boolean;
  resource_uuid: string;
}

export type SubscriptionPostResponseTypes = SubscriptionPostTypes & {
  uuid: string;
}

export type SubscriptionPatchTypes = {
  to_telegram: boolean;
  to_email: boolean;
  uuid: string;
}

export type SubscriptionGetResponseTypes = {
  to_telegram: boolean;
  to_email: boolean;
  uuid: string;
  resource_uuid?: string;
}

export type ReviewRequestTypes = {
  text: string;
  stars: number;
  resource_uuid: string;
}

export type ReportRequestTypes = {
  status: 'critical' | 'OK',
  is_moderated: false;
  uuid?: string;
  resource_uuid: string;
}

export type GetCheckResultsResponseTypes = {
  end_datetime: string;
  ok: number;
  partial: number;
  critical: number;
}

export type GetCheckResultsRequestTypes = {
  timedelta: number;
  max_count: number;
  source_uuid: string;
}

export type GetBotTokenResponseTypes = {
  token: string;
}

export type AdminPostResourceTypes = {
  name: string;
}

export type ResourceNode = {
  url: string,
  uuid: string
}