import React from 'react';
import {useParams} from "react-router-dom";

const User = () => {
    const params = useParams()
    console.log(params.user_id)

    return (
        <div>

        </div>
    );
};

export default User;