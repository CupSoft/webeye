import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'
import { GetCheckResultsRequestTypes, GetCheckResultsResponseTypes, ReportRequestTypes, ReviewGetTypes, ReviewRequestTypes, SocialReporGetTypes, SourceGetRequestTypes, SourceGetTypes, SubscriptionGetResponseTypes, SubscriptionPatchTypes, SubscriptionPostResponseTypes, SubscriptionPostTypes, UserLoginResponseTypes, UserRegistrRequestTypes, UserRegistrResponseTypes } from './apiServiceTypes'

class CreateRequest {
  public method: string;
  constructor (public url: string, public body: string | FormData, public headers?: {[key: string]: string | undefined}) {
    this.method = 'POST'
    this.url = url;
    this.body = body;
    this.headers = {'Content-Type': 'application/json', ...headers}
  }
}

export const api = createApi({
  reducerPath: 'api',
  baseQuery: fetchBaseQuery({
    baseUrl: `${process.env.REACT_APP_API_HOST}:${process.env.REACT_APP_API_PORT}/api/`,
    prepareHeaders(headers, {getState}) {
      const token = localStorage.getItem('token')

      if (token) {
        headers.set('Authorization', token)
      }

      return headers
    }
  }),
  tagTypes: ['User', 'Source'],
  endpoints: (builder) => ({
    registerUser: builder.mutation<UserRegistrResponseTypes, UserRegistrRequestTypes>({
      query: (user) => new CreateRequest('auth/users', JSON.stringify(user))
    }),
    loginUser: builder.mutation<UserLoginResponseTypes, FormData>({
      query: (user) => new CreateRequest('auth/login/access-token', user, {'Content-Type': undefined})
    }),
    checkUser: builder.mutation<UserRegistrResponseTypes, void>({
      query: () => ({url: 'auth/users/me'})
    }),
    getSource: builder.query<SourceGetTypes, string>({
      query: (sourceUuid) => ({ url: `resources/${sourceUuid}` })
    }),
    getAllSources: builder.query<SourceGetTypes[], SourceGetRequestTypes>({
      query: (params) => ({ 
        url: `resources`,
        params
      })
    }),
    getAllSocialReports: builder.query<SocialReporGetTypes[], string>({
      query: (sourceUuid) => ({ url: `resources/${sourceUuid}/social_reports`})
    }),
    getAllReviews: builder.query<ReviewGetTypes[], string>({
      query: (sourceUuid) => ({ url: `resources/${sourceUuid}/reviews` })
    }),
    postSubscriptions: builder.mutation<SubscriptionPostResponseTypes, SubscriptionPostTypes>({
      query: (subs) => new CreateRequest('subscriptions', JSON.stringify(subs))
    }),
    patchSubscriptions: builder.mutation<void, SubscriptionPatchTypes>({
      query: ({uuid, ...subs}) => ({
        method: 'PATCH',
        url: `subscriptions/${uuid}`,
        params: {...subs},
        headers: {'Content-Type': 'application/json'}
      })
    }),
    getSubscriptions: builder.query<SubscriptionGetResponseTypes[], string>({
      query: (resource_id) => ({ 
        url: `auth/users/me/subscriptions`,
        params: {resource_id}
      })
    }),
    postReview: builder.mutation<void, ReviewRequestTypes>({
      query: (review) => new CreateRequest('reviews', JSON.stringify(review))
    }),
    postReport: builder.mutation<void, ReportRequestTypes>({
      query: (report) => new CreateRequest('reports', JSON.stringify(report))
    }),
    getAllCheckResults: builder.query<GetCheckResultsResponseTypes[], GetCheckResultsRequestTypes>({
      query: ({source_uuid, ...params}) => ({
        params,
        url: `resources/${source_uuid}/stats/checks`
      })
    }),
  })
})

export const { useRegisterUserMutation } = api
export const { useLoginUserMutation } = api
export const { useGetAllSourcesQuery } = api
export const { useGetSourceQuery } = api
export const { useCheckUserMutation } = api
export const { useGetAllSocialReportsQuery } = api
export const { useGetAllReviewsQuery } = api
export const { usePostSubscriptionsMutation } = api
export const { useGetSubscriptionsQuery } = api
export const { usePatchSubscriptionsMutation } = api
export const { usePostReportMutation } = api
export const { usePostReviewMutation } = api
export const { useGetAllCheckResultsQuery } = api