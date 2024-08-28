# Testing

## Manual testing
- Manual testing was carried out on the deployed site.

| Location           | Feature                 | Expected Outcome                                                                                                                                                                                                                                          | Pass/Fail | Notes                                                                                                                                      |
| ------------------ | ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Header             | Home button             | Takes user to home page on click                                                                                                                                                                                                                          | PASS      |                                                                                                                                            |
| Header             | Log-in button           | Takes user to log-in page on click                                                                                                                                                                                                                        | PASS      | If user is not logged in, the register and log-in buttons will be displayed but if they are logged in, only the log-out button will appear |
| Header             | Register button         | Takes user to registration page on click                                                                                                                                                                                                                  | PASS      |
| Header             | Logout button           | Takes user to log-out page on click                                                                                                                                                                                                                       | PASS      |
| Log-in page        | Log-in function         | When user enters an unknown username, the user will not be logged in                                                                                                                                                                                      | PASS      |                                                                                                                                            |
| Log-in page        | Log-in function         | When user enters an unknown password, the user will not be logged in                                                                                                                                                                                      | PASS      |                                                                                                                                            |
| Log-in page        | Log-in function         | When user enters a known username AND password, the user will be logged in                                                                                                                                                                                | PASS      |                                                                                                                                            |
| Register page      | Register function       | If user does not enter information into any of the fields, they will be prompted to fill in the field                                                                                                                                                     | PASS      |                                                                                                                                            |
| Register page      | Register function       | If user does not enter a password which fits the criteria, will not be registered                                                                                                                                                                         | PASS      |                                                                                                                                            |
| Register page      | Register function       | If user does not enter a matching password into the password (again) box, they will not be registered                                                                                                                                                     | PASS      |                                                                                                                                            |
| Register page      | Register function       | If user enters appropriate details, they will be registered                                                                                                                                                                                               | PASS      |                                                                                                                                            |
| Logout page        | Sign out button         | Signs user out on click                                                                                                                                                                                                                                   | PASS      |                                                                                                                                            |
| Home page          | Staff review card       | Click on staff review to be taken to that review                                                                                                                                                                                                          | PASS      |                                                                                                                                            |
| Home page          | Next button             | If there are more than six staff reviews, a 'next' button will appear. On click, this will load the next six available staff reviews.                                                                                                                     | PASS      |                                                                                                                                            |
| Home page          | Prev button             | If there are more than six staff reviews, a 'next >>' button will appear. On click, this will load the next six available staff reviews. On this page, a '<<prev [previous]' button will appear. On click, this will load the previous six staff reviews' | PASS      |                                                                                                                                            |
| Footer             | Dog icon                | Clicking will take you to the 'Jerry Green Dog Rescue' page (it is a slow loading web-page)                                                                                                                                                               | PASS      |                                                                                                                                            |
| Footer             | Dog food icon           | Clicking will take you to the 'RSPCA' page                                                                                                                                                                                                                | PASS      |                                                                                                                                            |
| Footer             | Dog icon                | Clicking will take you to the 'East Midlands Dog Rescue' page                                                                                                                                                                                             | PASS      |                                                                                                                                            |
| Staff review       | Leave a review function | Leaving the 'Your review' box empty and clicking Submit will prompt the user to fill out the 'Your review' box                                                                                                                                            | PASS      |                                                                                                                                            |
| Staff review       | Leave a review function | Filling out the 'Your review' box and pressing Submit will submit the review for approval                                                                                                                                                                 | PASS      |                                                                                                                                            |
| Staff review       | Delete a review         | Pressing 'Delete' will delete the user review                                                                                                                                                                                                             | PASS      |                                                                                                                                            |
| Staff review       | Edit a review           | Pressing 'Edit' will open the 'Edit your review' page in a new tab                                                                                                                                                                                        | PASS      |                                                                                                                                            |
| Edit a review page | Edit a review           | Entering a review/rating and pressing submit will update review needing edited                                                                                                                                                                            | PASS      |                                                                                                                                            |

## User stories testing

## Bugs

## Code validators
### HTML
#### Home
- ![Home page validator screenshot](static/images/html-vali-home.png)

#### Logout page
- ![Logout page validator screenshot](static/images/html-vali-home.png)

#### Login page
- ![Login page validator screenshot](static/images/html-vali-home.png)

#### Register page
- ![Register page validator screenshot](static/images/html-val-register.png)
- When I checked the code that the validator was referring to, it was code which was integrated by Django for the review functionality and not written by me. I looked for it everywhere in an attempt to fix it but could not find it. 
- ![Register page validator screenshot code](static/images/html-val-register-code.png)

#### Example of Staff review (e.g. Bendigo Lounge)
- ![Staff review validator screenshot](static/images/html-val-review.png)
- The code which the validator is referring to is inputted from the admin section of the Django backend framework via summernote. It is not possible to add an 'alt' reference as a user. The </ p> is also code created by the framework.

#### Edit review page
- ![Edit review validator screenshot](static/images/html-vali-home.png)

### CSS
- ![CSS validator screenshot](static/images/css-vali.png)

<p>
    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
</p>
<p>
<a href="http://jigsaw.w3.org/css-validator/check/referer">
    <img style="border:0;width:88px;height:31px"
        src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
        alt="Valid CSS!" />
    </a>
</p>

### Python


### Lighthouse

## Responsiveness
#### Mobile (iPhone 14 Pro)

#### Tablet (iPad Air 5)

#### Desktop (Macbook Air)