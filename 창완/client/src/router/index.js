import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)


import MainView from '@/views/MainView.vue'
// 회원가입 및 탈퇴, 로그인 관련
import LoginView from '@/views/LoginView.vue'
import LogOutView from '@/views/LogOutView.vue'
import SignupView from '@/views/SignupView.vue'
import JobSeekerSignupView from '@/views/JobSeekerSignupView.vue'
import CompanySignupView from '@/views/CompanySignupView.vue'
import AcademySignupView from '@/views/AcademySignupView.vue'
import SignOutView from '@/views/SignOutView.vue'
import SignOutCompleteView from '@/views/SignOutCompleteView.vue'

// 개인 프로필
import JobSeekerProfileView from '@/views/JobSeekerProfileView.vue'
import JobSeekerProcessView from '@/views/JobSeekerProcessView.vue'
import JobSeekerApplyView from '@/views/JobSeekerApplyView.vue'
import JobSeekerSuggestView from '@/views/JobSeekerSuggestView.vue'

// 회사 프로필
import CompanyProfileView from '@/views/CompanyProfileView.vue'
import CompanyPostingView from '@/views/CompanyPostingView.vue'
import CompanySuggestView from '@/views/CompanySuggestView.vue'

// 학원 프로필
import AcademyProfileView from '@/views/AcademyProfileView.vue'
import AcademyPostingView from '@/views/AcademyPostingView.vue'

// 공고 등록
import JobPostingView from '@/views/JobPostingView.vue'
import EduPostingView from '@/views/EduPostingView.vue'
import PostingCompleteView from '@/views/PostingCompleteView.vue'

// 구직 관련 페이지
import JobListView from '@/views/JobListView.vue'
import JobDetailView from '@/views/JobDetailView.vue'
import JobApplyView from '@/views/JobApplyView.vue'
import JobApplyCompleteView from '@/views/JobApplyCompleteView.vue'

// 구인 관련 페이지
import JobSeekerListView from '@/views/JobSeekerListView.vue'
import JobSeekerDetailView from '@/views/JobSeekerDetailView.vue'
import JobOfferView from '@/views/JobOfferView.vue'
import JobOfferCompleteView from '@/views/JobOfferCompleteView.vue'

// 교육 관련 페이지
import AcademyCategoryView from '@/views/AcademyCategoryView.vue'
import AcademyListView from '@/views/AcademyListView.vue'
import EduDetailView from '@/views/EduDetailView.vue'
import EduApplyView from '@/views/EduApplyView.vue'
import EduApplyCompleteView from '@/views/EduApplyCompleteView.vue'

import NotFound404 from '@/views/NotFound404'


const routes = [
  {
    path: '/',
    name: 'main',
    component: MainView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/logout',
    name: 'logOut',
    component: LogOutView
  },
  {
    path: '/signup',
    name: 'singup',
    component: SignupView
  },
  {
    path: '/signup/jobseeker',
    name: 'jobseekerSignup',
    component: JobSeekerSignupView
  },
  {
    path: '/signup/company',
    name: 'companySignup',
    component: CompanySignupView
  },
  {
    path: '/signup/academy',
    name: 'academySignup',
    component: AcademySignupView
  },
  {
    path: '/signout',
    name: 'signout',
    component: SignOutView
  },
  {
    path: '/signout/complete',
    name: 'signoutComplete',
    component: SignOutCompleteView
  },
  {
    path: '/profile/company/:company_id',
    name: 'companyProfile',
    component: CompanyProfileView
  },
  {
    path: '/profile/company/:company_id/posting',
    name: 'companyPosting',
    component: CompanyPostingView
  },
  {
    path: '/profile/company/:company_id/suggest',
    name: 'companySuggest',
    component: CompanySuggestView
  },
  {
    path: '/profile/jobseeker/:jobseeker_id',
    name: 'jobSeekerProfile',
    component: JobSeekerProfileView
  },
  {
    path: '/profile/jobseeker/:jobseeker_id/process',
    name: 'jobSeekerProcess',
    component: JobSeekerProcessView
  },
  {
    path: '/profile/jobseeker/:jobseeker_id/apply',
    name: 'jobSeekerApply',
    component: JobSeekerApplyView 
  },
  {
    path: '/profile/jobseeker/:jobseeker_id/suggest',
    name: 'jobSeekerSuggest',
    component: JobSeekerSuggestView
  },
  {
    path: '/profile/academy/:academy_id',
    name: 'academyProfile',
    component: AcademyProfileView
  },
  {
    path: '/profile/academy/:academy_id/posting',
    name: 'academyPosting',
    component: AcademyPostingView
  },
  {
    path: '/jobposting',
    name: 'jobPosting',
    component: JobPostingView
  },
  {
    path: '/eduposting',
    name: 'eduPosting',
    component: EduPostingView
  },
  {
    path: '/postingcomplete',
    name: 'postingComplete',
    component: PostingCompleteView
  },
  {
    path: '/job',
    name: 'jobList',
    component: JobListView
  },
  {
    path: '/job/:job_id',
    name: 'jobDetail',
    component: JobDetailView
  },
  {
    path: '/job/:job_id/apply',
    name: 'jobApply',
    component: JobApplyView
  },
  {
    path: '/job/:job_id/complete',
    name: 'jobApplyComplete',
    component: JobApplyCompleteView
  },
  {
    path: '/jobseeker',
    name: 'jobSeekerList',
    component: JobSeekerListView
  },
  {
    path: '/jobseeker/:jobseeker_id',
    name: 'jobSeekerDetail',
    component: JobSeekerDetailView 
  },
  {
    path: '/jobseeker/:jobseeker_id/offer',
    name: 'jobOffer',
    component: JobOfferView
  },
  {
    path: '/jobseeker/:jobseeker/complete',
    name: 'jobOfferComplete',
    component: JobOfferCompleteView
  },
  {
    path: '/academy',
    name: 'academyCategory',
    component: AcademyCategoryView
  },
  {
    path: '/academy/:category_id',
    name: 'academyList',
    component: AcademyListView 
  },
  {
    path: '/academy/:edu_id',
    name: 'eduDetail',
    component: EduDetailView 
  },
  {
    path: '/academy/:edu_id/complete',
    name: 'eduApply',
    component: EduApplyView
  },
  {
    path: '/academy/:edu_id/complete',
    name: 'eduApplyComplete',
    component: EduApplyCompleteView 
  },
  {
    path: '/404',
    name: 'NotFound404',
    component : NotFound404
  },
  {
    path: '*',
    redirect: '/404'
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
