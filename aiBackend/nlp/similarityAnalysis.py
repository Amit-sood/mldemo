print('Printing from docker')
from sentence_transformers import SentenceTransformer, util
import numpy as np
from numpy.linalg import norm

modelPath="./models/"
model = SentenceTransformer(modelPath)

#model.save(modelPath)

#model = SentenceTransformer(modelPath)

searchSentence = 'James Abercrombie 8 Hanbury Drive'
searchSentenceArray=[]

sentences=['James Abercrombie 8 Hanbury Drive, Calcot RG31 7EJ (0118) 602 4786',
            'Amran Ahmad 34 Ashley Road, Bradford-On-Avon BA15 1RT (01225) 102717',
            'Steven Alexander Danes Court Cottage, Cartmel Fell LA11 6NT (015395) 64146',
            'Philip Andrews 4 Naas Lane, Lydney GL15 5AW (01594) 188536',
            'Iain Arbuckle 6 Churchill Avenue, Wellingborough NN8 5YG (01933) 127372',
            'Steven Bailey 39 Addison Crescent, Manchester M16 0WN (0161) 000 0058',
            'Tristan Bailey 22 Parkers Road, Crewe CW1 4GA (01270) 805443',
            'Anthony Bartlett 44 Cliff Road, Newquay TR7 2ND (01637) 405111',
            'Mark Bateman 8 Grenville Avenue, Goring By Sea BN12 6JE (01903) 714834',
            'Karina Batra 9 Warren Chase, Kesgrave IP5 2WZ (01473) 050287',
            'Rowena Beaton 11 Buttercup Square, Stanwell TW19 7UD (01784) 552224',
            'Maria Beattie 12A Allott Street, Hoyland S74 0NF (01226) 203378',
            'Young Bellis 34 Hilperton Road, Trowbridge BA14 7JD (01225) 372424',
            'Elizabeth Bennett 77 Cedarwood Glade, Stainton TS8 9DL (01642) 158401',
            'Stephen Black 88 Needham Drive, Workington CA14 3SE (01900) 427372',
            'Stuart Blank 128A Commercial Street, Maesteg CF34 9DW (01639) 608577',
            'Anne Bonnett Flat 3, Whitehaugh Court, Church Road, Eastleigh SO50 6DF (01489) 672467',
            'Anthony Bowen 42 Klondyke Way, Asfordby LE14 3TW (01664) 506383',
            'Stepehn Bradly 3 Gillford Crescent, Carlisle CA1 3BS (01228) 701144',
            'Amran Ahmad 34 Ashley Road, Bradford-On-Avon BA15 1RT (01225) 102717',
            'Steven Alexander Danes Court Cottage, Cartmel Fell LA11 6NT (015395) 64146',
            'Philip Andrews 4 Naas Lane, Lydney GL15 5AW (01594) 188536',
            'Iain Arbuckle 6 Churchill Avenue, Wellingborough NN8 5YG (01933) 127372',
            'Steven Bailey 39 Addison Crescent, Manchester M16 0WN (0161) 000 0058',
            'Tristan Bailey 22 Parkers Road, Crewe CW1 4GA (01270) 805443',
            'Anthony Bartlett 44 Cliff Road, Newquay TR7 2ND (01637) 405111',
            'Mark Bateman 8 Grenville Avenue, Goring By Sea BN12 6JE (01903) 714834',
            'Karina Batra 9 Warren Chase, Kesgrave IP5 2WZ (01473) 050287',
            'Rowena Beaton 11 Buttercup Square, Stanwell TW19 7UD (01784) 552224',
            'Maria Beattie 12A Allott Street, Hoyland S74 0NF (01226) 203378',
            'Young Bellis 34 Hilperton Road, Trowbridge BA14 7JD (01225) 372424',
            'Elizabeth Bennett 77 Cedarwood Glade, Stainton TS8 9DL (01642) 158401',
            'Stephen Black 88 Needham Drive, Workington CA14 3SE (01900) 427372',
            'Stuart Blank 128A Commercial Street, Maesteg CF34 9DW (01639) 608577',
            'Anne Bonnett Flat 3, Whitehaugh Court, Church Road, Eastleigh SO50 6DF (01489) 672467',
            'Anthony Bowen 42 Klondyke Way, Asfordby LE14 3TW (01664) 506383',
            'Stepehn Bradly 3 Gillford Crescent, Carlisle CA1 3BS (01228) 701144',
            'Amran Ahmad 34 Ashley Road, Bradford-On-Avon BA15 1RT (01225) 102717',
            'Steven Alexander Danes Court Cottage, Cartmel Fell LA11 6NT (015395) 64146',
            'Philip Andrews 4 Naas Lane, Lydney GL15 5AW (01594) 188536',
            'Iain Arbuckle 6 Churchill Avenue, Wellingborough NN8 5YG (01933) 127372',
            'Steven Bailey 39 Addison Crescent, Manchester M16 0WN (0161) 000 0058',
            'Tristan Bailey 22 Parkers Road, Crewe CW1 4GA (01270) 805443',
            'Anthony Bartlett 44 Cliff Road, Newquay TR7 2ND (01637) 405111',
            'Mark Bateman 8 Grenville Avenue, Goring By Sea BN12 6JE (01903) 714834',
            'Karina Batra 9 Warren Chase, Kesgrave IP5 2WZ (01473) 050287',
            'Rowena Beaton 11 Buttercup Square, Stanwell TW19 7UD (01784) 552224',
            'Maria Beattie 12A Allott Street, Hoyland S74 0NF (01226) 203378',
            'Young Bellis 34 Hilperton Road, Trowbridge BA14 7JD (01225) 372424',
            'Elizabeth Bennett 77 Cedarwood Glade, Stainton TS8 9DL (01642) 158401',
            'Stephen Black 88 Needham Drive, Workington CA14 3SE (01900) 427372',
            'Stuart Blank 128A Commercial Street, Maesteg CF34 9DW (01639) 608577',
            'Anne Bonnett Flat 3, Whitehaugh Court, Church Road, Eastleigh SO50 6DF (01489) 672467',
            'Anthony Bowen 42 Klondyke Way, Asfordby LE14 3TW (01664) 506383',
            'Stepehn Bradly 3 Gillford Crescent, Carlisle CA1 3BS (01228) 701144',
            'Amran Ahmad 34 Ashley Road, Bradford-On-Avon BA15 1RT (01225) 102717',
            'Steven Alexander Danes Court Cottage, Cartmel Fell LA11 6NT (015395) 64146',
            'Philip Andrews 4 Naas Lane, Lydney GL15 5AW (01594) 188536',
            'Iain Arbuckle 6 Churchill Avenue, Wellingborough NN8 5YG (01933) 127372',
            'Steven Bailey 39 Addison Crescent, Manchester M16 0WN (0161) 000 0058',
            'Tristan Bailey 22 Parkers Road, Crewe CW1 4GA (01270) 805443',
            'Anthony Bartlett 44 Cliff Road, Newquay TR7 2ND (01637) 405111',
            'Mark Bateman 8 Grenville Avenue, Goring By Sea BN12 6JE (01903) 714834',
            'Karina Batra 9 Warren Chase, Kesgrave IP5 2WZ (01473) 050287',
            'Rowena Beaton 11 Buttercup Square, Stanwell TW19 7UD (01784) 552224',
            'Maria Beattie 12A Allott Street, Hoyland S74 0NF (01226) 203378',
            'Young Bellis 34 Hilperton Road, Trowbridge BA14 7JD (01225) 372424',
            'Elizabeth Bennett 77 Cedarwood Glade, Stainton TS8 9DL (01642) 158401',
            'Stephen Black 88 Needham Drive, Workington CA14 3SE (01900) 427372',
            'Stuart Blank 128A Commercial Street, Maesteg CF34 9DW (01639) 608577',
            'Anne Bonnett Flat 3, Whitehaugh Court, Church Road, Eastleigh SO50 6DF (01489) 672467',
            'Anthony Bowen 42 Klondyke Way, Asfordby LE14 3TW (01664) 506383',
            'Stepehn Bradly 3 Gillford Crescent, Carlisle CA1 3BS (01228) 701144',
            'Amran Ahmad 34 Ashley Road, Bradford-On-Avon BA15 1RT (01225) 102717',
            'Steven Alexander Danes Court Cottage, Cartmel Fell LA11 6NT (015395) 64146',
            'Philip Andrews 4 Naas Lane, Lydney GL15 5AW (01594) 188536',
            'Iain Arbuckle 6 Churchill Avenue, Wellingborough NN8 5YG (01933) 127372',
            'Steven Bailey 39 Addison Crescent, Manchester M16 0WN (0161) 000 0058',
            'Tristan Bailey 22 Parkers Road, Crewe CW1 4GA (01270) 805443',
            'Anthony Bartlett 44 Cliff Road, Newquay TR7 2ND (01637) 405111',
            'Mark Bateman 8 Grenville Avenue, Goring By Sea BN12 6JE (01903) 714834',
            'Karina Batra 9 Warren Chase, Kesgrave IP5 2WZ (01473) 050287',
            'Rowena Beaton 11 Buttercup Square, Stanwell TW19 7UD (01784) 552224',
            'Maria Beattie 12A Allott Street, Hoyland S74 0NF (01226) 203378',
            'Young Bellis 34 Hilperton Road, Trowbridge BA14 7JD (01225) 372424',
            'Elizabeth Bennett 77 Cedarwood Glade, Stainton TS8 9DL (01642) 158401',
            'Stephen Black 88 Needham Drive, Workington CA14 3SE (01900) 427372',
            'Stuart Blank 128A Commercial Street, Maesteg CF34 9DW (01639) 608577',
            'Anne Bonnett Flat 3, Whitehaugh Court, Church Road, Eastleigh SO50 6DF (01489) 672467',
            'Anthony Bowen 42 Klondyke Way, Asfordby LE14 3TW (01664) 506383',
            'Stepehn Bradly 3 Gillford Crescent, Carlisle CA1 3BS (01228) 701144',
            'Amran Ahmad 34 Ashley Road, Bradford-On-Avon BA15 1RT (01225) 102717',
            'Steven Alexander Danes Court Cottage, Cartmel Fell LA11 6NT (015395) 64146',
            'Philip Andrews 4 Naas Lane, Lydney GL15 5AW (01594) 188536',
            'Iain Arbuckle 6 Churchill Avenue, Wellingborough NN8 5YG (01933) 127372',
            'Steven Bailey 39 Addison Crescent, Manchester M16 0WN (0161) 000 0058',
            'Tristan Bailey 22 Parkers Road, Crewe CW1 4GA (01270) 805443',
            'Anthony Bartlett 44 Cliff Road, Newquay TR7 2ND (01637) 405111',
            'Mark Bateman 8 Grenville Avenue, Goring By Sea BN12 6JE (01903) 714834',
            'Karina Batra 9 Warren Chase, Kesgrave IP5 2WZ (01473) 050287',
            'Rowena Beaton 11 Buttercup Square, Stanwell TW19 7UD (01784) 552224',
            'Maria Beattie 12A Allott Street, Hoyland S74 0NF (01226) 203378',
            'Young Bellis 34 Hilperton Road, Trowbridge BA14 7JD (01225) 372424',
            'Elizabeth Bennett 77 Cedarwood Glade, Stainton TS8 9DL (01642) 158401',
            'Stephen Black 88 Needham Drive, Workington CA14 3SE (01900) 427372',
            'Stuart Blank 128A Commercial Street, Maesteg CF34 9DW (01639) 608577',
            'Anne Bonnett Flat 3, Whitehaugh Court, Church Road, Eastleigh SO50 6DF (01489) 672467',
            'Anthony Bowen 42 Klondyke Way, Asfordby LE14 3TW (01664) 506383',
            'Stepehn Bradly 3 Gillford Crescent, Carlisle CA1 3BS (01228) 701144',
            'Amran Ahmad 34 Ashley Road, Bradford-On-Avon BA15 1RT (01225) 102717',
            'Steven Alexander Danes Court Cottage, Cartmel Fell LA11 6NT (015395) 64146',
            'Philip Andrews 4 Naas Lane, Lydney GL15 5AW (01594) 188536',
            'Iain Arbuckle 6 Churchill Avenue, Wellingborough NN8 5YG (01933) 127372',
            'Steven Bailey 39 Addison Crescent, Manchester M16 0WN (0161) 000 0058',
            'Tristan Bailey 22 Parkers Road, Crewe CW1 4GA (01270) 805443',
            'Anthony Bartlett 44 Cliff Road, Newquay TR7 2ND (01637) 405111',
            'Mark Bateman 8 Grenville Avenue, Goring By Sea BN12 6JE (01903) 714834',
            'Karina Batra 9 Warren Chase, Kesgrave IP5 2WZ (01473) 050287',
            'Rowena Beaton 11 Buttercup Square, Stanwell TW19 7UD (01784) 552224',
            'Maria Beattie 12A Allott Street, Hoyland S74 0NF (01226) 203378',
            'Young Bellis 34 Hilperton Road, Trowbridge BA14 7JD (01225) 372424',
            'Elizabeth Bennett 77 Cedarwood Glade, Stainton TS8 9DL (01642) 158401',
            'Stephen Black 88 Needham Drive, Workington CA14 3SE (01900) 427372',
            'Stuart Blank 128A Commercial Street, Maesteg CF34 9DW (01639) 608577',
            'Anne Bonnett Flat 3, Whitehaugh Court, Church Road, Eastleigh SO50 6DF (01489) 672467',
            'Anthony Bowen 42 Klondyke Way, Asfordby LE14 3TW (01664) 506383',
            'Stepehn Bradly 3 Gillford Crescent, Carlisle CA1 3BS (01228) 701144',
            'Amran Ahmad 34 Ashley Road, Bradford-On-Avon BA15 1RT (01225) 102717',
            'Steven Alexander Danes Court Cottage, Cartmel Fell LA11 6NT (015395) 64146',
            'Philip Andrews 4 Naas Lane, Lydney GL15 5AW (01594) 188536',
            'Iain Arbuckle 6 Churchill Avenue, Wellingborough NN8 5YG (01933) 127372',
            'Steven Bailey 39 Addison Crescent, Manchester M16 0WN (0161) 000 0058',
            'Tristan Bailey 22 Parkers Road, Crewe CW1 4GA (01270) 805443',
            'Anthony Bartlett 44 Cliff Road, Newquay TR7 2ND (01637) 405111',
            'Mark Bateman 8 Grenville Avenue, Goring By Sea BN12 6JE (01903) 714834',
            'Karina Batra 9 Warren Chase, Kesgrave IP5 2WZ (01473) 050287',
            'Rowena Beaton 11 Buttercup Square, Stanwell TW19 7UD (01784) 552224',
            'Maria Beattie 12A Allott Street, Hoyland S74 0NF (01226) 203378',
            'Young Bellis 34 Hilperton Road, Trowbridge BA14 7JD (01225) 372424',
            'Elizabeth Bennett 77 Cedarwood Glade, Stainton TS8 9DL (01642) 158401',
            'Stephen Black 88 Needham Drive, Workington CA14 3SE (01900) 427372',
            'Stuart Blank 128A Commercial Street, Maesteg CF34 9DW (01639) 608577',
            'Anne Bonnett Flat 3, Whitehaugh Court, Church Road, Eastleigh SO50 6DF (01489) 672467',
            'Anthony Bowen 42 Klondyke Way, Asfordby LE14 3TW (01664) 506383',
            'Stepehn Bradly 3 Gillford Crescent, Carlisle CA1 3BS (01228) 701144',
            'Amran Ahmad 34 Ashley Road, Bradford-On-Avon BA15 1RT (01225) 102717',
            'Steven Alexander Danes Court Cottage, Cartmel Fell LA11 6NT (015395) 64146',
            'Philip Andrews 4 Naas Lane, Lydney GL15 5AW (01594) 188536',
            'Iain Arbuckle 6 Churchill Avenue, Wellingborough NN8 5YG (01933) 127372',
            'Steven Bailey 39 Addison Crescent, Manchester M16 0WN (0161) 000 0058',
            'Tristan Bailey 22 Parkers Road, Crewe CW1 4GA (01270) 805443',
            'Anthony Bartlett 44 Cliff Road, Newquay TR7 2ND (01637) 405111',
            'Mark Bateman 8 Grenville Avenue, Goring By Sea BN12 6JE (01903) 714834',
            'Karina Batra 9 Warren Chase, Kesgrave IP5 2WZ (01473) 050287',
            'Rowena Beaton 11 Buttercup Square, Stanwell TW19 7UD (01784) 552224',
            'Maria Beattie 12A Allott Street, Hoyland S74 0NF (01226) 203378',
            'Young Bellis 34 Hilperton Road, Trowbridge BA14 7JD (01225) 372424',
            'Elizabeth Bennett 77 Cedarwood Glade, Stainton TS8 9DL (01642) 158401',
            'Stephen Black 88 Needham Drive, Workington CA14 3SE (01900) 427372',
            'Stuart Blank 128A Commercial Street, Maesteg CF34 9DW (01639) 608577',
            'Anne Bonnett Flat 3, Whitehaugh Court, Church Road, Eastleigh SO50 6DF (01489) 672467',
            'Anthony Bowen 42 Klondyke Way, Asfordby LE14 3TW (01664) 506383',
            'Stepehn Bradly 3 Gillford Crescent, Carlisle CA1 3BS (01228) 701144',
            'Amran Ahmad 34 Ashley Road, Bradford-On-Avon BA15 1RT (01225) 102717',
            'Steven Alexander Danes Court Cottage, Cartmel Fell LA11 6NT (015395) 64146',
            'Philip Andrews 4 Naas Lane, Lydney GL15 5AW (01594) 188536',
            'Iain Arbuckle 6 Churchill Avenue, Wellingborough NN8 5YG (01933) 127372',
            'Steven Bailey 39 Addison Crescent, Manchester M16 0WN (0161) 000 0058',
            'Tristan Bailey 22 Parkers Road, Crewe CW1 4GA (01270) 805443',
            'Anthony Bartlett 44 Cliff Road, Newquay TR7 2ND (01637) 405111',
            'Mark Bateman 8 Grenville Avenue, Goring By Sea BN12 6JE (01903) 714834',
            'Karina Batra 9 Warren Chase, Kesgrave IP5 2WZ (01473) 050287',
            'Rowena Beaton 11 Buttercup Square, Stanwell TW19 7UD (01784) 552224',
            'Maria Beattie 12A Allott Street, Hoyland S74 0NF (01226) 203378',
            'Young Bellis 34 Hilperton Road, Trowbridge BA14 7JD (01225) 372424',
            'Elizabeth Bennett 77 Cedarwood Glade, Stainton TS8 9DL (01642) 158401',
            'Stephen Black 88 Needham Drive, Workington CA14 3SE (01900) 427372',
            'Stuart Blank 128A Commercial Street, Maesteg CF34 9DW (01639) 608577',
            'Anne Bonnett Flat 3, Whitehaugh Court, Church Road, Eastleigh SO50 6DF (01489) 672467',
            'Anthony Bowen 42 Klondyke Way, Asfordby LE14 3TW (01664) 506383',
            'Stepehn Bradly 3 Gillford Crescent, Carlisle CA1 3BS (01228) 701144',
            'Amran Ahmad 34 Ashley Road, Bradford-On-Avon BA15 1RT (01225) 102717',
            'Steven Alexander Danes Court Cottage, Cartmel Fell LA11 6NT (015395) 64146',
            'Philip Andrews 4 Naas Lane, Lydney GL15 5AW (01594) 188536',
            'Iain Arbuckle 6 Churchill Avenue, Wellingborough NN8 5YG (01933) 127372',
            'Steven Bailey 39 Addison Crescent, Manchester M16 0WN (0161) 000 0058',
            'Tristan Bailey 22 Parkers Road, Crewe CW1 4GA (01270) 805443',
            'Anthony Bartlett 44 Cliff Road, Newquay TR7 2ND (01637) 405111',
            'Mark Bateman 8 Grenville Avenue, Goring By Sea BN12 6JE (01903) 714834',
            'Karina Batra 9 Warren Chase, Kesgrave IP5 2WZ (01473) 050287',
            'Rowena Beaton 11 Buttercup Square, Stanwell TW19 7UD (01784) 552224',
            'Maria Beattie 12A Allott Street, Hoyland S74 0NF (01226) 203378',
            'Young Bellis 34 Hilperton Road, Trowbridge BA14 7JD (01225) 372424',
            'Elizabeth Bennett 77 Cedarwood Glade, Stainton TS8 9DL (01642) 158401',
            'Stephen Black 88 Needham Drive, Workington CA14 3SE (01900) 427372',
            'Stuart Blank 128A Commercial Street, Maesteg CF34 9DW (01639) 608577',
            'Anne Bonnett Flat 3, Whitehaugh Court, Church Road, Eastleigh SO50 6DF (01489) 672467',
            'Anthony Bowen 42 Klondyke Way, Asfordby LE14 3TW (01664) 506383',
            'Stepehn Bradly 3 Gillford Crescent, Carlisle CA1 3BS (01228) 701144',
            'Amran Ahmad 34 Ashley Road, Bradford-On-Avon BA15 1RT (01225) 102717',
            'Steven Alexander Danes Court Cottage, Cartmel Fell LA11 6NT (015395) 64146',
            'Philip Andrews 4 Naas Lane, Lydney GL15 5AW (01594) 188536',
            'Iain Arbuckle 6 Churchill Avenue, Wellingborough NN8 5YG (01933) 127372',
            'Steven Bailey 39 Addison Crescent, Manchester M16 0WN (0161) 000 0058',
            'Tristan Bailey 22 Parkers Road, Crewe CW1 4GA (01270) 805443',
            'Anthony Bartlett 44 Cliff Road, Newquay TR7 2ND (01637) 405111',
            'Mark Bateman 8 Grenville Avenue, Goring By Sea BN12 6JE (01903) 714834',
            'Karina Batra 9 Warren Chase, Kesgrave IP5 2WZ (01473) 050287',
            'Rowena Beaton 11 Buttercup Square, Stanwell TW19 7UD (01784) 552224',
            'Maria Beattie 12A Allott Street, Hoyland S74 0NF (01226) 203378',
            'Young Bellis 34 Hilperton Road, Trowbridge BA14 7JD (01225) 372424',
            'Elizabeth Bennett 77 Cedarwood Glade, Stainton TS8 9DL (01642) 158401',
            'Stephen Black 88 Needham Drive, Workington CA14 3SE (01900) 427372',
            'Stuart Blank 128A Commercial Street, Maesteg CF34 9DW (01639) 608577',
            'Anne Bonnett Flat 3, Whitehaugh Court, Church Road, Eastleigh SO50 6DF (01489) 672467',
            'Anthony Bowen 42 Klondyke Way, Asfordby LE14 3TW (01664) 506383',
            'Stepehn Bradly 3 Gillford Crescent, Carlisle CA1 3BS (01228) 701144',
            'Amran Ahmad 34 Ashley Road, Bradford-On-Avon BA15 1RT (01225) 102717',
            'Steven Alexander Danes Court Cottage, Cartmel Fell LA11 6NT (015395) 64146',
            'Philip Andrews 4 Naas Lane, Lydney GL15 5AW (01594) 188536',
            'Iain Arbuckle 6 Churchill Avenue, Wellingborough NN8 5YG (01933) 127372',
            'Steven Bailey 39 Addison Crescent, Manchester M16 0WN (0161) 000 0058',
            'Tristan Bailey 22 Parkers Road, Crewe CW1 4GA (01270) 805443',
            'Anthony Bartlett 44 Cliff Road, Newquay TR7 2ND (01637) 405111',
            'Mark Bateman 8 Grenville Avenue, Goring By Sea BN12 6JE (01903) 714834',
            'Karina Batra 9 Warren Chase, Kesgrave IP5 2WZ (01473) 050287',
            'Rowena Beaton 11 Buttercup Square, Stanwell TW19 7UD (01784) 552224',
            'Maria Beattie 12A Allott Street, Hoyland S74 0NF (01226) 203378',
            'Young Bellis 34 Hilperton Road, Trowbridge BA14 7JD (01225) 372424',
            'Elizabeth Bennett 77 Cedarwood Glade, Stainton TS8 9DL (01642) 158401',
            'Stephen Black 88 Needham Drive, Workington CA14 3SE (01900) 427372',
            'Stuart Blank 128A Commercial Street, Maesteg CF34 9DW (01639) 608577',
            'Anne Bonnett Flat 3, Whitehaugh Court, Church Road, Eastleigh SO50 6DF (01489) 672467',
            'Anthony Bowen 42 Klondyke Way, Asfordby LE14 3TW (01664) 506383',
            'Stepehn Bradly 3 Gillford Crescent, Carlisle CA1 3BS (01228) 701144',
            'Amran Ahmad 34 Ashley Road, Bradford-On-Avon BA15 1RT (01225) 102717',
            'Steven Alexander Danes Court Cottage, Cartmel Fell LA11 6NT (015395) 64146',
            'Philip Andrews 4 Naas Lane, Lydney GL15 5AW (01594) 188536',
            'Iain Arbuckle 6 Churchill Avenue, Wellingborough NN8 5YG (01933) 127372',
            'Steven Bailey 39 Addison Crescent, Manchester M16 0WN (0161) 000 0058',
            'Tristan Bailey 22 Parkers Road, Crewe CW1 4GA (01270) 805443',
            'Anthony Bartlett 44 Cliff Road, Newquay TR7 2ND (01637) 405111',
            'Mark Bateman 8 Grenville Avenue, Goring By Sea BN12 6JE (01903) 714834',
            'Karina Batra 9 Warren Chase, Kesgrave IP5 2WZ (01473) 050287',
            'Rowena Beaton 11 Buttercup Square, Stanwell TW19 7UD (01784) 552224',
            'Maria Beattie 12A Allott Street, Hoyland S74 0NF (01226) 203378',
            'Young Bellis 34 Hilperton Road, Trowbridge BA14 7JD (01225) 372424',
            'Elizabeth Bennett 77 Cedarwood Glade, Stainton TS8 9DL (01642) 158401',
            'Stephen Black 88 Needham Drive, Workington CA14 3SE (01900) 427372',
            'Stuart Blank 128A Commercial Street, Maesteg CF34 9DW (01639) 608577',
            'Anne Bonnett Flat 3, Whitehaugh Court, Church Road, Eastleigh SO50 6DF (01489) 672467',
            'Anthony Bowen 42 Klondyke Way, Asfordby LE14 3TW (01664) 506383',
            'Stepehn Bradly 3 Gillford Crescent, Carlisle CA1 3BS (01228) 701144',
            'Amran Ahmad 34 Ashley Road, Bradford-On-Avon BA15 1RT (01225) 102717',
            'Steven Alexander Danes Court Cottage, Cartmel Fell LA11 6NT (015395) 64146',
            'Philip Andrews 4 Naas Lane, Lydney GL15 5AW (01594) 188536',
            'Iain Arbuckle 6 Churchill Avenue, Wellingborough NN8 5YG (01933) 127372',
            'Steven Bailey 39 Addison Crescent, Manchester M16 0WN (0161) 000 0058',
            'Tristan Bailey 22 Parkers Road, Crewe CW1 4GA (01270) 805443',
            'Anthony Bartlett 44 Cliff Road, Newquay TR7 2ND (01637) 405111',
            'Mark Bateman 8 Grenville Avenue, Goring By Sea BN12 6JE (01903) 714834',
            'Karina Batra 9 Warren Chase, Kesgrave IP5 2WZ (01473) 050287',
            'Rowena Beaton 11 Buttercup Square, Stanwell TW19 7UD (01784) 552224',
            'Maria Beattie 12A Allott Street, Hoyland S74 0NF (01226) 203378',
            'Young Bellis 34 Hilperton Road, Trowbridge BA14 7JD (01225) 372424',
            'Elizabeth Bennett 77 Cedarwood Glade, Stainton TS8 9DL (01642) 158401',
            'Stephen Black 88 Needham Drive, Workington CA14 3SE (01900) 427372',
            'Stuart Blank 128A Commercial Street, Maesteg CF34 9DW (01639) 608577',
            'Anne Bonnett Flat 3, Whitehaugh Court, Church Road, Eastleigh SO50 6DF (01489) 672467',
            'Anthony Bowen 42 Klondyke Way, Asfordby LE14 3TW (01664) 506383',
            'Stepehn Bradly 3 Gillford Crescent, Carlisle CA1 3BS (01228) 701144',
            'Steven Bailey 39 Addison Crescent, Manchester M16 0WN (0161) 000 0058',
            'Tristan Bailey 22 Parkers Road, Crewe CW1 4GA (01270) 805443',
            'Anthony Bartlett 44 Cliff Road, Newquay TR7 2ND (01637) 405111',
            'Mark Bateman 8 Grenville Avenue, Goring By Sea BN12 6JE (01903) 714834',
            'Karina Batra 9 Warren Chase, Kesgrave IP5 2WZ (01473) 050287',
            'Rowena Beaton 11 Buttercup Square, Stanwell TW19 7UD (01784) 552224',
            'Maria Beattie 12A Allott Street, Hoyland S74 0NF (01226) 203378',
            'Young Bellis 34 Hilperton Road, Trowbridge BA14 7JD (01225) 372424',
            'Elizabeth Bennett 77 Cedarwood Glade, Stainton TS8 9DL (01642) 158401',
            'Stephen Black 88 Needham Drive, Workington CA14 3SE (01900) 427372',
            'Stuart Blank 128A Commercial Street, Maesteg CF34 9DW (01639) 608577',
            'Anne Bonnett Flat 3, Whitehaugh Court, Church Road, Eastleigh SO50 6DF (01489) 672467',
            'Anthony Bowen 42 Klondyke Way, Asfordby LE14 3TW (01664) 506383',
            'Stepehn Bradly 3 Gillford Crescent, Carlisle CA1 3BS (01228) 701144',
            'Amran Ahmad 34 Ashley Road, Bradford-On-Avon BA15 1RT (01225) 102717',
            'Steven Alexander Danes Court Cottage, Cartmel Fell LA11 6NT (015395) 64146',
            'Philip Andrews 4 Naas Lane, Lydney GL15 5AW (01594) 188536',
            'Iain Arbuckle 6 Churchill Avenue, Wellingborough NN8 5YG (01933) 127372',
            'Steven Bailey 39 Addison Crescent, Manchester M16 0WN (0161) 000 0058',
            'Tristan Bailey 22 Parkers Road, Crewe CW1 4GA (01270) 805443',
            'Anthony Bartlett 44 Cliff Road, Newquay TR7 2ND (01637) 405111',
            'Mark Bateman 8 Grenville Avenue, Goring By Sea BN12 6JE (01903) 714834',
            'Karina Batra 9 Warren Chase, Kesgrave IP5 2WZ (01473) 050287',
            'Rowena Beaton 11 Buttercup Square, Stanwell TW19 7UD (01784) 552224',
            'Maria Beattie 12A Allott Street, Hoyland S74 0NF (01226) 203378',
            'Young Bellis 34 Hilperton Road, Trowbridge BA14 7JD (01225) 372424',
            'Elizabeth Bennett 77 Cedarwood Glade, Stainton TS8 9DL (01642) 158401',
            'Stephen Black 88 Needham Drive, Workington CA14 3SE (01900) 427372',
            'Stuart Blank 128A Commercial Street, Maesteg CF34 9DW (01639) 608577',
            'Anne Bonnett Flat 3, Whitehaugh Court, Church Road, Eastleigh SO50 6DF (01489) 672467',
            'Anthony Bowen 42 Klondyke Way, Asfordby LE14 3TW (01664) 506383',
            'Stepehn Bradly 3 Gillford Crescent, Carlisle CA1 3BS (01228) 701144',
            'Amran Ahmad 34 Ashley Road, Bradford-On-Avon BA15 1RT (01225) 102717',
            'Steven Alexander Danes Court Cottage, Cartmel Fell LA11 6NT (015395) 64146',
            'Philip Andrews 4 Naas Lane, Lydney GL15 5AW (01594) 188536',
            'Iain Arbuckle 6 Churchill Avenue, Wellingborough NN8 5YG (01933) 127372',
            'Steven Bailey 39 Addison Crescent, Manchester M16 0WN (0161) 000 0058',
            'Tristan Bailey 22 Parkers Road, Crewe CW1 4GA (01270) 805443',
            'Anthony Bartlett 44 Cliff Road, Newquay TR7 2ND (01637) 405111',
            'Mark Bateman 8 Grenville Avenue, Goring By Sea BN12 6JE (01903) 714834',
            'Karina Batra 9 Warren Chase, Kesgrave IP5 2WZ (01473) 050287',
            'Rowena Beaton 11 Buttercup Square, Stanwell TW19 7UD (01784) 552224',
            'Maria Beattie 12A Allott Street, Hoyland S74 0NF (01226) 203378',
            'Young Bellis 34 Hilperton Road, Trowbridge BA14 7JD (01225) 372424',
            'Elizabeth Bennett 77 Cedarwood Glade, Stainton TS8 9DL (01642) 158401',
            'Stephen Black 88 Needham Drive, Workington CA14 3SE (01900) 427372',
            'Stuart Blank 128A Commercial Street, Maesteg CF34 9DW (01639) 608577',
            'Anne Bonnett Flat 3, Whitehaugh Court, Church Road, Eastleigh SO50 6DF (01489) 672467',
            'Anthony Bowen 42 Klondyke Way, Asfordby LE14 3TW (01664) 506383',
            'Stepehn Bradly 3 Gillford Crescent, Carlisle CA1 3BS (01228) 701144',
            'Amran Ahmad 34 Ashley Road, Bradford-On-Avon BA15 1RT (01225) 102717',
            'Steven Alexander Danes Court Cottage, Cartmel Fell LA11 6NT (015395) 64146',
            'Philip Andrews 4 Naas Lane, Lydney GL15 5AW (01594) 188536',
            'Iain Arbuckle 6 Churchill Avenue, Wellingborough NN8 5YG (01933) 127372',
            'Steven Bailey 39 Addison Crescent, Manchester M16 0WN (0161) 000 0058',
            'Tristan Bailey 22 Parkers Road, Crewe CW1 4GA (01270) 805443',
            'Anthony Bartlett 44 Cliff Road, Newquay TR7 2ND (01637) 405111',
            'Mark Bateman 8 Grenville Avenue, Goring By Sea BN12 6JE (01903) 714834',
            'Karina Batra 9 Warren Chase, Kesgrave IP5 2WZ (01473) 050287',
            'Rowena Beaton 11 Buttercup Square, Stanwell TW19 7UD (01784) 552224',
            'Maria Beattie 12A Allott Street, Hoyland S74 0NF (01226) 203378',
            'Young Bellis 34 Hilperton Road, Trowbridge BA14 7JD (01225) 372424',
            'Elizabeth Bennett 77 Cedarwood Glade, Stainton TS8 9DL (01642) 158401',
            'Stephen Black 88 Needham Drive, Workington CA14 3SE (01900) 427372',
            'Stuart Blank 128A Commercial Street, Maesteg CF34 9DW (01639) 608577',
            'Anne Bonnett Flat 3, Whitehaugh Court, Church Road, Eastleigh SO50 6DF (01489) 672467',
            'Anthony Bowen 42 Klondyke Way, Asfordby LE14 3TW (01664) 506383',
            'Stepehn Bradly 3 Gillford Crescent, Carlisle CA1 3BS (01228) 701144',
            'Amran Ahmad 34 Ashley Road, Bradford-On-Avon BA15 1RT (01225) 102717',
            'Steven Alexander Danes Court Cottage, Cartmel Fell LA11 6NT (015395) 64146',
            'Philip Andrews 4 Naas Lane, Lydney GL15 5AW (01594) 188536',
            'Iain Arbuckle 6 Churchill Avenue, Wellingborough NN8 5YG (01933) 127372',
            'Steven Bailey 39 Addison Crescent, Manchester M16 0WN (0161) 000 0058',
            'Tristan Bailey 22 Parkers Road, Crewe CW1 4GA (01270) 805443',
            'Anthony Bartlett 44 Cliff Road, Newquay TR7 2ND (01637) 405111',
            'Mark Bateman 8 Grenville Avenue, Goring By Sea BN12 6JE (01903) 714834',
            'Karina Batra 9 Warren Chase, Kesgrave IP5 2WZ (01473) 050287',
            'Rowena Beaton 11 Buttercup Square, Stanwell TW19 7UD (01784) 552224',
            'Maria Beattie 12A Allott Street, Hoyland S74 0NF (01226) 203378',
            'Young Bellis 34 Hilperton Road, Trowbridge BA14 7JD (01225) 372424',
            'Elizabeth Bennett 77 Cedarwood Glade, Stainton TS8 9DL (01642) 158401',
            'Stephen Black 88 Needham Drive, Workington CA14 3SE (01900) 427372',
            'Stuart Blank 128A Commercial Street, Maesteg CF34 9DW (01639) 608577',
            'Anne Bonnett Flat 3, Whitehaugh Court, Church Road, Eastleigh SO50 6DF (01489) 672467',
            'Anthony Bowen 42 Klondyke Way, Asfordby LE14 3TW (01664) 506383',
            'Stepehn Bradly 3 Gillford Crescent, Carlisle CA1 3BS (01228) 701144',
            'Steven Bailey 39 Addison Crescent, Manchester M16 0WN (0161) 000 0058',
            'Tristan Bailey 22 Parkers Road, Crewe CW1 4GA (01270) 805443',
            'Anthony Bartlett 44 Cliff Road, Newquay TR7 2ND (01637) 405111',
            'Mark Bateman 8 Grenville Avenue, Goring By Sea BN12 6JE (01903) 714834',
            'Karina Batra 9 Warren Chase, Kesgrave IP5 2WZ (01473) 050287',
            'Rowena Beaton 11 Buttercup Square, Stanwell TW19 7UD (01784) 552224',
            'Maria Beattie 12A Allott Street, Hoyland S74 0NF (01226) 203378',
            'Young Bellis 34 Hilperton Road, Trowbridge BA14 7JD (01225) 372424',
            'Elizabeth Bennett 77 Cedarwood Glade, Stainton TS8 9DL (01642) 158401',
            'Stephen Black 88 Needham Drive, Workington CA14 3SE (01900) 427372',
            'Stuart Blank 128A Commercial Street, Maesteg CF34 9DW (01639) 608577',
            'Anne Bonnett Flat 3, Whitehaugh Court, Church Road, Eastleigh SO50 6DF (01489) 672467',
            'Anthony Bowen 42 Klondyke Way, Asfordby LE14 3TW (01664) 506383',
            'Stepehn Bradly 3 Gillford Crescent, Carlisle CA1 3BS (01228) 701144',
            'Amran Ahmad 34 Ashley Road, Bradford-On-Avon BA15 1RT (01225) 102717',
            'Steven Alexander Danes Court Cottage, Cartmel Fell LA11 6NT (015395) 64146',
            'Philip Andrews 4 Naas Lane, Lydney GL15 5AW (01594) 188536',
            'Iain Arbuckle 6 Churchill Avenue, Wellingborough NN8 5YG (01933) 127372',
            'Steven Bailey 39 Addison Crescent, Manchester M16 0WN (0161) 000 0058',
            'Tristan Bailey 22 Parkers Road, Crewe CW1 4GA (01270) 805443',
            'Anthony Bartlett 44 Cliff Road, Newquay TR7 2ND (01637) 405111',
            'Mark Bateman 8 Grenville Avenue, Goring By Sea BN12 6JE (01903) 714834',
            'Karina Batra 9 Warren Chase, Kesgrave IP5 2WZ (01473) 050287',
            'Rowena Beaton 11 Buttercup Square, Stanwell TW19 7UD (01784) 552224',
            'Maria Beattie 12A Allott Street, Hoyland S74 0NF (01226) 203378',
            'Young Bellis 34 Hilperton Road, Trowbridge BA14 7JD (01225) 372424',
            'Elizabeth Bennett 77 Cedarwood Glade, Stainton TS8 9DL (01642) 158401',
            'Stephen Black 88 Needham Drive, Workington CA14 3SE (01900) 427372',
            'Stuart Blank 128A Commercial Street, Maesteg CF34 9DW (01639) 608577',
            'Anne Bonnett Flat 3, Whitehaugh Court, Church Road, Eastleigh SO50 6DF (01489) 672467',
            'Anthony Bowen 42 Klondyke Way, Asfordby LE14 3TW (01664) 506383',
            'Stepehn Bradly 3 Gillford Crescent, Carlisle CA1 3BS (01228) 701144',
            'Amran Ahmad 34 Ashley Road, Bradford-On-Avon BA15 1RT (01225) 102717',
            'Steven Alexander Danes Court Cottage, Cartmel Fell LA11 6NT (015395) 64146',
            'Philip Andrews 4 Naas Lane, Lydney GL15 5AW (01594) 188536',
            'Iain Arbuckle 6 Churchill Avenue, Wellingborough NN8 5YG (01933) 127372',
            'Steven Bailey 39 Addison Crescent, Manchester M16 0WN (0161) 000 0058',
            'Tristan Bailey 22 Parkers Road, Crewe CW1 4GA (01270) 805443',
            'Anthony Bartlett 44 Cliff Road, Newquay TR7 2ND (01637) 405111',
            'Mark Bateman 8 Grenville Avenue, Goring By Sea BN12 6JE (01903) 714834',
            'Karina Batra 9 Warren Chase, Kesgrave IP5 2WZ (01473) 050287',
            'Rowena Beaton 11 Buttercup Square, Stanwell TW19 7UD (01784) 552224',
            'Maria Beattie 12A Allott Street, Hoyland S74 0NF (01226) 203378',
            'Young Bellis 34 Hilperton Road, Trowbridge BA14 7JD (01225) 372424',
            'Elizabeth Bennett 77 Cedarwood Glade, Stainton TS8 9DL (01642) 158401',
            'Stephen Black 88 Needham Drive, Workington CA14 3SE (01900) 427372',
            'Stuart Blank 128A Commercial Street, Maesteg CF34 9DW (01639) 608577',
            'Anne Bonnett Flat 3, Whitehaugh Court, Church Road, Eastleigh SO50 6DF (01489) 672467',
            'Anthony Bowen 42 Klondyke Way, Asfordby LE14 3TW (01664) 506383',
            'Stepehn Bradly 3 Gillford Crescent, Carlisle CA1 3BS (01228) 701144',
            'Amran Ahmad 34 Ashley Road, Bradford-On-Avon BA15 1RT (01225) 102717',
            'Steven Alexander Danes Court Cottage, Cartmel Fell LA11 6NT (015395) 64146',
            'Philip Andrews 4 Naas Lane, Lydney GL15 5AW (01594) 188536',
            'Iain Arbuckle 6 Churchill Avenue, Wellingborough NN8 5YG (01933) 127372',
            'Steven Bailey 39 Addison Crescent, Manchester M16 0WN (0161) 000 0058',
            'Tristan Bailey 22 Parkers Road, Crewe CW1 4GA (01270) 805443',
            'Anthony Bartlett 44 Cliff Road, Newquay TR7 2ND (01637) 405111',
            'Mark Bateman 8 Grenville Avenue, Goring By Sea BN12 6JE (01903) 714834',
            'Karina Batra 9 Warren Chase, Kesgrave IP5 2WZ (01473) 050287',
            'Rowena Beaton 11 Buttercup Square, Stanwell TW19 7UD (01784) 552224',
            'Maria Beattie 12A Allott Street, Hoyland S74 0NF (01226) 203378',
            'Young Bellis 34 Hilperton Road, Trowbridge BA14 7JD (01225) 372424',
            'Elizabeth Bennett 77 Cedarwood Glade, Stainton TS8 9DL (01642) 158401',
            'Stephen Black 88 Needham Drive, Workington CA14 3SE (01900) 427372',
            'Stuart Blank 128A Commercial Street, Maesteg CF34 9DW (01639) 608577',
            'Anne Bonnett Flat 3, Whitehaugh Court, Church Road, Eastleigh SO50 6DF (01489) 672467',
            'Anthony Bowen 42 Klondyke Way, Asfordby LE14 3TW (01664) 506383',
            'Stepehn Bradly 3 Gillford Crescent, Carlisle CA1 3BS (01228) 701144',
            'Amran Ahmad 34 Ashley Road, Bradford-On-Avon BA15 1RT (01225) 102717',
            'Steven Alexander Danes Court Cottage, Cartmel Fell LA11 6NT (015395) 64146',
            'Philip Andrews 4 Naas Lane, Lydney GL15 5AW (01594) 188536',
            'Iain Arbuckle 6 Churchill Avenue, Wellingborough NN8 5YG (01933) 127372',
            'Steven Bailey 39 Addison Crescent, Manchester M16 0WN (0161) 000 0058',
            'Tristan Bailey 22 Parkers Road, Crewe CW1 4GA (01270) 805443',
            'Anthony Bartlett 44 Cliff Road, Newquay TR7 2ND (01637) 405111',
            'Mark Bateman 8 Grenville Avenue, Goring By Sea BN12 6JE (01903) 714834',
            'Karina Batra 9 Warren Chase, Kesgrave IP5 2WZ (01473) 050287',
            'Rowena Beaton 11 Buttercup Square, Stanwell TW19 7UD (01784) 552224',
            'Maria Beattie 12A Allott Street, Hoyland S74 0NF (01226) 203378',
            'Young Bellis 34 Hilperton Road, Trowbridge BA14 7JD (01225) 372424',
            'Elizabeth Bennett 77 Cedarwood Glade, Stainton TS8 9DL (01642) 158401',
            'Stephen Black 88 Needham Drive, Workington CA14 3SE (01900) 427372',
            'Stuart Blank 128A Commercial Street, Maesteg CF34 9DW (01639) 608577',
            'Anne Bonnett Flat 3, Whitehaugh Court, Church Road, Eastleigh SO50 6DF (01489) 672467',
            'Anthony Bowen 42 Klondyke Way, Asfordby LE14 3TW (01664) 506383',
            'Stepehn Bradly 3 Gillford Crescent, Carlisle CA1 3BS (01228) 701144',
            'David Bradney Awel Mon, Marianglas LL73 8PF (01248) 858652',
            'Chris Bramham 3 Lower Grosvenor Place, London SW1W 0EJ (020) 8310 6207',
            'Scott Bramley 82 Jordan Avenue, Stretton DE13 0JB (01283) 540112',
            'Mary Brown 109A Havant Road, Drayton PO6 2AH (01329) 482088',
            'Strachan Bruce 10 Evesham Close, Boldon Colliery NE35 9LL (0191) 708 7845',
            'Agnes Buntain Foxpark Farm, Newton Le Willows DL8 1RZ (01677) 356575',
            'Stephen Burd 6 John Street, Swan Village B70 0AB (01384) 187473',
            'Barbara Butler 3 Little Court Close, Midhurst GU29 9SS (01428) 837643',
            'Margaret Carr The Old Vicarage, Crosthwaite LA8 8BP (01539) 406041',
            'Anne Carruth Eastfield, Roughton Moor LN10 6YQ (01526) 523308',
            'Ryan Carson 78 Altrincham Road, Gatley SK8 4DZ (0161) 306 8330',
            'Paul Clifton Glanrhyd Uchaf, Boncath SA37 0JY (01239) 544620']


for i in range(len(sentences)):    
    searchSentenceArray.append(searchSentence)


#singleSearchEmbeddings = model.encode(searchSentence, convert_to_tensor=False)

#singleSearchEmbeddings
#print(singleSearchEmbeddings)


#Compute embeddings
#embeddings_withoutTensor = model.encode(sentences, convert_to_tensor=False)
#all_embeddings = np.array(embeddings_withoutTensor)
#np.save('./models/embeddings_withoutTensor.npy', all_embeddings)


#searchEmbeddings = model.encode(searchSentence, convert_to_tensor=False)
#embeddings=np.load('./models/embeddings_withoutTensor.npy')
#corpus_embeddings = util.normalize_embeddings(embeddings)
#query_embeddings = util.normalize_embeddings(searchEmbeddings)
#hits = util.semantic_search(embeddings, searchEmbeddings, score_function=util.dot_score)
#print('****************')
#print(len(hits))



#Compute embeddings
#embeddings = model.encode(sentences, convert_to_tensor=True)
#all_embeddings = np.array(embeddings)
#np.save('./models/embeddings.npy', all_embeddings)

embeddings=np.load('./models/embeddings.npy')

searchEmbeddings = model.encode(searchSentenceArray, convert_to_tensor=True)
searchSentenceArray=[]
for i in range(len(sentences)):    
    searchSentenceArray.append(searchEmbeddings)



print('-----------------')

#Compute cosine-similarities for each sentence with each other sentence
cosine_scores = util.cos_sim(searchEmbeddings, embeddings)



#Output the pairs with their score
for i in range(len(sentences)):
    print("{} \t\t {} \t\t Score: {:.4f}".format(sentences[i], searchSentenceArray[i], cosine_scores[i][i]))

