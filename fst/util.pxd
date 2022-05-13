from libcpp.string cimport string

cdef extern from "<iostream>" namespace "std":
    cdef cppclass ostream:
        pass
    cdef cppclass istream:
        pass
    cdef cppclass ostringstream(ostream):
        ostringstream()
        string str()
    cdef cppclass ifstream(istream):
        ifstream(char* filename)

cdef extern from "<sstream>" namespace "std" nogil:

  cdef cppclass stringstream(istream, ostream):

    stringstream()

    string str()

    stringstream &operator<<(const string &)

    stringstream &operator<<(bool)

    # We define these in terms of the Google cintegral_types.

    stringstream &operator<<(int8)

    stringstream &operator<<(uint8)

    stringstream &operator<<(int16)

    stringstream &operator<<(uint16)

    stringstream &operator<<(int32)

    stringstream &operator<<(uint32)

    stringstream &operator<<(int64)

    stringstream &operator<<(uint64)

    stringstream &operator<<(double)

    stringstream &operator<<(long double)
