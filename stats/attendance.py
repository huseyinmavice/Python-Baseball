import pandas as pd
import matplotlib.pyplot as plt
from data import games

#mask = (games['type']=='info') & (games['multi2']=='attendance')
attendance = games.loc[(games['type']=='info') & (games['multi2']=='attendance'), ['year', 'multi3'] ]

attendance.columns = ['year', 'attendance']

attendance.loc[:, 'attendance'] = pd.to_numeric(attendance.loc[:, 'attendance'])

print(attendance.head(5))

attendance.plot(kind='bar', x='year', y='attendance', figsize=(15,7))
plt.xlabel('Year')
plt.ylabel('Attendance')
plt.axhline(y=attendance['attendance'].mean(), label='Mean', linestyle='--',color='green')

plt.show()
