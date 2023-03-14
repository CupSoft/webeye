import React from 'react';
import { useGetAllReportsQuery } from '../../../services/apiService/apiService';

const ReportsForm = () => {
  const {data: reports, isLoading} = useGetAllReportsQuery()

  if (isLoading) {
    return null
  }

  return (
    <div className='admin_container'>
      <div className='admin_wrapper'>
        <h3 className='admin_title'>Заявки о доступности ресурсов</h3>
          {/* {reports?.map(report =>
            <ReportBadge/>
          )} */}
      </div>
    </div>
  );
};

export default ReportsForm;