import React from 'react';
import { useGetAllReportsQuery } from '../../../services/apiService/apiService';
import ReportBadge from '../ReportBadge/ReportBadge';

const ReportsForm = () => {
  const {data: reports, isLoading} = useGetAllReportsQuery()

  if (isLoading) {
    return null
  }
  console.log(reports)
  return (
    <div className='admin_container'>
      <div className='admin_wrapper'>
        <h3 className='admin_title'>Заявки о доступности ресурсов</h3>
          {reports?.map(report =>
            <ReportBadge key={report.uuid} {...report}/>
          )}
      </div>
    </div>
  );
};

export default ReportsForm;