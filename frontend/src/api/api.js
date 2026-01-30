import request from './request'

// 获取用户信息（传customer_id）
export const getCustomerInfo = (customer_id) => {
  return request.get(`/customers/${customer_id}/`)
}