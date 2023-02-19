import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'
import { ReportRequestTypes, ReviewGetTypes, ReviewRequestTypes, SocialReporGetTypes, SourceGetTypes, SubscriptionGetResponseTypes, SubscriptionPostTypes, UserLoginResponseTypes, UserRegistrRequestTypes, UserRegistrResponseTypes } from './apiServiceTypes'

class CreatePostRequest {
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
      query: (user) => new CreatePostRequest('auth/users', JSON.stringify(user))
    }),
    loginUser: builder.mutation<UserLoginResponseTypes, FormData>({
      query: (user) => new CreatePostRequest('auth/login/access-token', user, {'Content-Type': undefined})
    }),
    checkUser: builder.mutation<UserRegistrResponseTypes, void>({
      query: () => ({url: 'auth/users/me'})
    }),
    getSource: builder.query<SourceGetTypes, string>({
      query: (sourceUuid) => ({ url: `resources/${sourceUuid}` })
    }),
    getAllSources: builder.query<SourceGetTypes[], void>({
      query: () => ({ url: `resources`})
    }),
    getAllSocialReports: builder.query<SocialReporGetTypes[], string>({
      query: (sourceUuid) => ({ url: `resources/${sourceUuid}/social_reports`})
    }),
    getAllReviews: builder.query<ReviewGetTypes[], string>({
      query: (sourceUuid) => ({ url: `resources/${sourceUuid}/reviews` })
    }),
    postSubscriptions: builder.mutation<void, SubscriptionPostTypes>({
      query: (subs) => new CreatePostRequest('subscriptions', JSON.stringify(subs))
    }),
    getSubscriptions: builder.mutation<SubscriptionGetResponseTypes, string>({
      query: (sourceUuid) => ({ url: `subscriptions/${sourceUuid}`})
    }),
    postReview: builder.mutation<void, ReviewRequestTypes>({
      query: (review) => new CreatePostRequest('reviews', JSON.stringify(review))
    }),
    postReport: builder.mutation<void, ReportRequestTypes>({
      query: (report) => new CreatePostRequest('reports', JSON.stringify(report))
    })
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
export const { useGetSubscriptionsMutation } = api
export const { usePostReportMutation } = api
export const { usePostReviewMutation } = api