import { useGetSourceReportsQuery } from '../../../services/apiService/apiService';
import ReportBadge from '../../ReportBadge/ReportBadge';
import { ReportsListPropsType } from './ReportsListTypes';
import styles from './ReportsList.module.scss'

const ReportsList = ({sourceUuid, sourceName}: ReportsListPropsType) => {
  let {data: reports, isLoading} = useGetSourceReportsQuery(sourceUuid);

  if (reports) {
    reports = [...reports].filter(report => report.is_moderated)
  }

  if (isLoading) {
    return null;
  }

  return (
    <div className={styles.container}>
      {reports?.length 
        ? <>
            {reports && reports.map(report =>
            <ReportBadge 
              showModerated={true}
              key={report.uuid} 
              {...report}
              resource_name={sourceName}
            />
          )}
          </>
        : <span className={styles.no_reports}>Сообщений нет</span>
      }
    </div>
  );
};

export default ReportsList;