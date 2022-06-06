prediction = scrape_players_predict(driver)
        print(prediction)

    #     # Get the future points
    #     Names = driver.find_elements(by=By.XPATH, value='//tbody/tr/td/div/a')
    #     PtsPredict = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[27]')

    #     # Create the fpl_data dictionary
    #     fpl_predict = []

    #     # For the length of all the players available, put them in the fpl_data dictionary. But I have realised you can run calculations straight from here as well which is AMAZING!!!
    #     for i in range(len(Names)):
    #         temp_data = {
    #                     'Names': Names[i].text,
    #                     'PointsPredict': (PtsPredict[i].text)
    #         }
    #         fpl_predict.append(temp_data)        

    #     random_sleeps()

    # #     # sleep(10)

    # #     # print(fpl_data)
    # #     # print()
    # #     # print(fpl_data2)
    # #     # # Move sliders back to original positon


    #     # Turn the fpl_data into Panda DataFrame
    #     data2 = pd.DataFrame(fpl_predict)

        # Merge all the dataFrames using the Name column to match the data across dataFrames 
        data_all = data.merge(prediction, how='left', on='Names')

        # Fill all blanks in the dataframe with zeros so the results don't return NaN
        data_all.fillna(0, inplace=True)

        print(data_all)

        data_all.to_excel(f"Players with Predicted Points Scrape - {strftime('%a %d %b %Y %H %M %S %p')}.xlsx", index=False)